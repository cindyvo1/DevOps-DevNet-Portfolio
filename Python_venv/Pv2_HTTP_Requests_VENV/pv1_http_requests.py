"""
Pv1 – HTTP Requests lab (slides 20–35)
Voorbeeld van GET en POST naar https://httpbin.org
"""

import requests


def do_get():
    """Stuur een GET-request met query parameters."""
    url = "https://httpbin.org/get"
    params = {"key1": "value1", "key2": "value2"}

    r = requests.get(url, params=params, timeout=5)
    r.raise_for_status()  # error als geen 2xx

    data = r.json()
    print("=== GET /get ===")
    print("Status code:", r.status_code)
    print("URL:", data["url"])
    print("Args:", data["args"])
    print()


def do_post():
    """Stuur een POST-request met form data."""
    url = "https://httpbin.org/post"
    payload = {"username": "cindy", "role": "devops-student"}

    r = requests.post(url, data=payload, timeout=5)
    r.raise_for_status()

    data = r.json()
    print("=== POST /post ===")
    print("Status code:", r.status_code)
    print("URL:", data["url"])
    print("Form data terug:", data["form"])
    print()


def main():
    print("Pv1 – HTTP Requests lab")
    do_get()
    do_post()


if __name__ == "__main__":
    main()
