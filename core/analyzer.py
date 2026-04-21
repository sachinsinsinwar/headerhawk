HEADERS_TO_CHECK = {
    "strict-transport-security": {
        "risk": "Critical",
        "attack": "SSL stripping / MITM — attacker intercepts and downgrades HTTPS to HTTP"
    },
    "content-security-policy": {
        "risk": "Critical",
        "attack": "XSS — attacker injects malicious scripts, steals session cookies"
    },
    "access-control-allow-origin": {
        "risk": "Critical",
        "attack": "CORS misconfiguration — cross-origin requests steal authenticated data"
    },
    "x-frame-options": {
        "risk": "High",
        "attack": "Clickjacking — attacker embeds site in iframe, tricks user into clicking"
    },
    "x-content-type-options": {
        "risk": "High",
        "attack": "MIME sniffing — browser executes uploaded files as scripts"
    },
    "referrer-policy": {
        "risk": "Medium",
        "attack": "URL data leakage — sensitive tokens in URL leak to third parties"
    },
    "permissions-policy": {
        "risk": "Medium",
        "attack": "Feature abuse — unauthorized access to camera, mic, location"
    },
    "cache-control": {
        "risk": "Medium",
        "attack": "Sensitive data cached — auth pages found in shared/public browsers"
    },
    "x-xss-protection": {
        "risk": "Medium",
        "attack": "Reflected XSS — exploits legacy browsers without XSS filter"
    },
}

RISK_SCORE = {"Critical": 30, "High": 15, "Medium": 5}

def analyze(headers):
    headers_lower = {k.lower(): v for k, v in headers.items()}
    findings = []
    score = 100

    for header, info in HEADERS_TO_CHECK.items():
        if header not in headers_lower:
            findings.append({
                "header": header,
                "status": "MISSING",
                "risk": info["risk"],
                "attack": info["attack"]
            })
            score -= RISK_SCORE[info["risk"]]
        else:
            findings.append({
                "header": header,
                "status": "PRESENT",
                "risk": info["risk"],
                "value": headers_lower[header],
                "attack": ""
            })

    info_disclosure = []
    for h in ["server", "x-powered-by", "x-aspnet-version"]:
        if h in headers_lower:
            info_disclosure.append(f"{h}: {headers_lower[h]}")

    return {
        "findings": findings,
        "score": max(score, 0),
        "info_disclosure": info_disclosure
    }
