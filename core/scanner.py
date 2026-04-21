import requests

def get_headers(url):
    if not url.startswith("http"):
        url = "https://" + url

    try:
        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True,
            headers={"User-Agent": "HeaderHawk/1.0 Security Scanner"}
        )
        return {
            "url": url,
            "status_code": response.status_code,
            "headers": dict(response.headers)
        }
    except requests.exceptions.SSLError:
        try:
            response = requests.get(url, timeout=10, verify=False)
            return {
                "url": url,
                "status_code": response.status_code,
                "headers": dict(response.headers)
            }
        except Exception as e:
            return {"url": url, "error": str(e)}
    except Exception as e:
        return {"url": url, "error": str(e)}
