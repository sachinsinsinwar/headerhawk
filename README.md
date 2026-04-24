# 🦅 HeaderHawk

> Security Header Analyzer — Built for Pentesters, DevOps, and Developers

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Kali%20Linux-red)

HeaderHawk scans any website for missing HTTP security headers, assigns risk scores, explains real attack scenarios, and generates shareable HTML reports.

---

## Features

- Checks 9 critical security headers
- Risk scoring — Critical / High / Medium
- Shows real attack scenario for each missing header
- Detects server info disclosure (version leakage)
- Generates HTML report
- CI/CD ready — fail builds on missing critical headers
- Works on Kali Linux, Ubuntu, macOS

---

## Installation

\`\`\`bash
git clone https://github.com/sachinsinsinwar/headerhawk.git
cd headerhawk
pip install -r requirements.txt
\`\`\`

---

## Usage

\`\`\`bash
# Basic scan
python -m cli.main --url https://target.com

# Generate HTML report
python -m cli.main --url https://target.com --report html

# CI/CD — exit code 1 if critical headers missing
python -m cli.main --url https://target.com --fail-on critical

# Help
python -m cli.main -h
\`\`\`

---

## Example Output

\`\`\`
Target: https://example.com
Status Code: 200
Security Score: 30/100

Header                        Status    Risk      Attack Scenario
strict-transport-security     PRESENT   Critical  —
content-security-policy       MISSING   Critical  XSS — attacker injects malicious scripts
x-frame-options               MISSING   High      Clickjacking — attacker embeds site in iframe
\`\`\`

---

## Headers Checked

| Header | Risk | Attack if Missing |
|---|---|---|
| Strict-Transport-Security | Critical | SSL stripping / MITM |
| Content-Security-Policy | Critical | XSS attacks |
| Access-Control-Allow-Origin | Critical | CORS misconfiguration |
| X-Frame-Options | High | Clickjacking |
| X-Content-Type-Options | High | MIME sniffing |
| Referrer-Policy | Medium | URL data leakage |
| Permissions-Policy | Medium | Feature abuse |
| Cache-Control | Medium | Sensitive data cached |
| X-XSS-Protection | Medium | Reflected XSS |

---

## Who Is This For

**Pentester / Attacker** — Recon phase. Find missing headers on target, understand what attacks are possible.

**Security Engineer** — Scan UAT before formal VAPT. Fix issues before the auditor finds them.

**DevOps** — Add to GitHub Actions pipeline. Block deployments if critical headers are missing.

**Developer** — Compare staging vs production. Catch header mismatches before release.

---

## Created By

**Sachin Singh** — DevSecOps Engineer  
[LinkedIn](https://linkedin.com/in/sachin-sinsinwar) | [GitHub](https://github.com/sachinsinsinwar)

---

## License

MIT
