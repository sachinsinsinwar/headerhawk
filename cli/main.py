import argparse
import sys
from rich.console import Console
from rich.table import Table
from core.scanner import get_headers
from core.analyzer import analyze

console = Console()

BANNER = r"""
 _   _                _             _   _               _    
| | | | ___  __ _  __| | ___ _ __  | | | | __ ___      | | __
| |_| |/ _ \/ _` |/ _` |/ _ \ '__| | |_| |/ _` \ \ /\ / / |/ /
|  _  |  __/ (_| | (_| |  __/ |    |  _  | (_| |\ V  V /|   < 
|_| |_|\___|\__,_|\__,_|\___|_|    |_| |_|\__,_| \_/\_/ |_|\_\
"""

RISK_COLORS = {
    "Critical": "bold red",
    "High": "bold yellow",
    "Medium": "bold blue"
}

def print_banner():
    console.print(f"[cyan]{BANNER}[/cyan]")
    console.print("[bold white]        Security Header Analyzer — by Sachin Singh[/bold white]")
    console.print("[dim]        github.com/sachinsinsinwar/headerhawk[/dim]\n")

def print_results(result, findings, score, info_disclosure, fail_on=None):
    console.print(f"\n[bold]Target:[/bold] {result['url']}")
    console.print(f"[bold]Status Code:[/bold] {result['status_code']}")

    score_color = "green" if score >= 70 else "yellow" if score >= 40 else "red"
    console.print(f"[bold]Security Score:[/bold] [{score_color}]{score}/100[/{score_color}]\n")

    table = Table(show_header=True, header_style="bold cyan", expand=True)
    table.add_column("Header", style="dim", width=35)
    table.add_column("Status", width=10)
    table.add_column("Risk", width=10)
    table.add_column("Attack Scenario")

    fail = False
    for f in findings:
        if f["status"] == "MISSING":
            status = "[red]MISSING[/red]"
            attack = f["attack"]
            risk_style = RISK_COLORS.get(f["risk"], "white")
            risk = f"[{risk_style}]{f['risk']}[/{risk_style}]"
            if fail_on and f["risk"].lower() == fail_on.lower():
                fail = True
        else:
            status = "[green]PRESENT[/green]"
            attack = "[dim]—[/dim]"
            risk_style = RISK_COLORS.get(f["risk"], "white")
            risk = f"[{risk_style}]{f['risk']}[/{risk_style}]"

        table.add_row(f["header"], status, risk, attack)

    console.print(table)

    if info_disclosure:
        console.print("\n[bold red]Info Disclosure Detected:[/bold red]")
        for item in info_disclosure:
            console.print(f"  [yellow]{item}[/yellow]")

    if fail:
        console.print(f"\n[bold red]FAIL: Critical headers missing. Exiting with code 1.[/bold red]")
        sys.exit(1)

def main():
    print_banner()

    parser = argparse.ArgumentParser(
        prog="headerhawk",
        description="Security Header Analyzer — HeaderHawk"
    )
    parser.add_argument("--url", required=True, help="Target URL to scan")
    parser.add_argument("--report", choices=["html"], help="Generate report (html)")
    parser.add_argument("--fail-on", choices=["critical", "high", "medium"],
                        help="Exit with code 1 if this risk level is found missing (for CI/CD)")

    args = parser.parse_args()

    console.print(f"[dim]Scanning {args.url} ...[/dim]\n")

    result = get_headers(args.url)

    if "error" in result:
        console.print(f"[bold red]Error:[/bold red] {result['error']}")
        sys.exit(1)

    analysis = analyze(result["headers"])

    print_results(
        result,
        analysis["findings"],
        analysis["score"],
        analysis["info_disclosure"],
        fail_on=args.fail_on
    )

    if args.report == "html":
        from reports.html_report import generate
        filename = generate(
            result["url"],
            result["status_code"],
            analysis["score"],
            analysis["findings"],
            analysis["info_disclosure"]
        )
        console.print(f"\n[bold green]HTML report saved:[/bold green] {filename}")

if __name__ == "__main__":
    main()
