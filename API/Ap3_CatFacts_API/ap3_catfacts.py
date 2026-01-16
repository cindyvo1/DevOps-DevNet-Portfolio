"""
Ap3 – Eigen API-experiment (Python)

Dit script haalt random kattenfeiten op via een publieke REST-API:
https://catfact.ninja/fact
"""

import requests


URL = "https://catfact.ninja/fact"


def get_cat_fact() -> str:
    """Stuur een GET-request naar de API en geef de tekst van het feit terug."""
    response = requests.get(URL, timeout=5)

    # Fout gooien als status code geen 2xx is
    response.raise_for_status()

    data = response.json()
    return data.get("fact", "Geen feit ontvangen")


def main() -> None:
    print("=== Ap3 – Eigen API-experiment: Cat Facts ===")

    for i in range(3):
        fact = get_cat_fact()
        print(f"{i + 1}. {fact}")


if __name__ == "__main__":
    main()
