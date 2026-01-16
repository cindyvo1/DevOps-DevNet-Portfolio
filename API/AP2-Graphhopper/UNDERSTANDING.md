# Begrip – GraphHopper Routing API Lab

## Wat is het doel van dit lab?

Het doel van dit lab is begrijpen hoe een Python-script communiceert met een externe Routing-API om locaties te geocoden, routes te berekenen en instructies op te vragen via HTTP-requests.

## Wat doet het script?

Het script stuurt HTTP-verzoeken (requests) naar de GraphHopper API om:

- locaties om te zetten naar coördinaten (geocoding)
- routes te berekenen tussen twee plaatsen
- afstand en reistijd te berekenen
- turn-by-turn instructies weer te geven
- verschillende voertuigprofielen te testen (`car`, `bike`, `foot`)

## Waarom heb ik een API key nodig?

De GraphHopper API vereist authenticatie via een persoonlijke API key. Zonder geldige key worden geen routes berekend en krijg je een foutmelding of ongeldige response.

## Welke gegevens geeft de API terug?

De API-response bevat o.a.:

- `lat` + `lng` (geocoding)
- totale afstand (in meter)
- totale reistijd (in milliseconden)
- lijst met instructies
- gebruikte profiel (car/bike/foot)
- HTTP-statuscodes

De meest gebruikte stukken JSON worden geparsed en in de terminal getoond.

## Wat heb ik hieruit geleerd?

- Hoe je HTTP-requests uitvoert vanuit Python
- Hoe JSON data verwerkt en geparsed wordt
- Hoe REST API’s communiceren met applicaties
- Dat input validatie nodig is om foute user input op te vangen
- Dat API’s vaak raw data teruggeven zonder visuele interface
- Dat verschillende profielen (car/bike/foot) andere routes opleveren
- Dat foutcodes en statuscodes belangrijke debug-informatie zijn

## Link met DevOps

Dit experiment toont hoe applicaties met elkaar communiceren via REST-API’s — één van de basisconcepten van moderne microservices en CI/CD-architecturen.  
Routing, data-uitwisseling en API-integratie zijn kernonderdelen in geautomatiseerde systemen en infrastructure-as-code workflows.
