# Ap3 – Eigen API-experiment (Cat Facts)

## Doel
Een eigen Python-script maken dat een REST-API aanroept en JSON-gegevens verwerkt.

## Concept
Een API (Application Programming Interface) maakt het mogelijk om data op te vragen of acties uit te voeren via HTTP requests.
In dit experiment wordt een **GET-request** gebruikt.

## Gebruikte API
Publieke API:
https://catfact.ninja/fact

Response voorbeeld (JSON):
```json
{
  "fact": "Cats sleep for 70% of their lives.",
  "length": 35
}
## Werking
1.Python stuurt een GET-request → requests.get()

2.De API stuurt JSON terug

3.JSON wordt geconverteerd naar een Python-dict

4.Het script toont drie random feiten in de terminal

## Waarom hoort dit bij DevOps?

DevOps-applicaties communiceren vaak via REST-API’s voor:

- monitoring

- automatisatie

- provisioning

- configuratie

- data-uitwisseling

Het kunnen gebruiken van een REST-API is daarom essentieel.
