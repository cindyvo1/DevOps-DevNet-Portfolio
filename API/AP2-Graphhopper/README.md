# Lab 4.9.2 – GraphHopper Routing API

**Doel:**  
Werken met een externe Routing-API (GraphHopper) om locaties te geocoden, routes te berekenen en turn-by-turn instructies op te vragen via Python scripts.

**Technologie:**

- Python
- REST API
- JSON
- HTTP requests (requests library)
- CLI input handling

**Wat heb ik gedaan:**

- Locaties opgezocht via de GraphHopper **geocoding API**
- Een Python-functie geschreven om geocoding-resultaten (lat/lon) uit JSON te halen  
- User input toegevoegd voor vertrekpunt en bestemming (+ `q/quit` om af te sluiten)
- Foutafhandeling toegevoegd voor:
  - lege input
  - ongeldige locaties
  - foutieve API-responses
- Routes opgevraagd via de **routing API**
- Afstand en reistijd berekend:
  - kilometer en miles
  - tijd in `hh:mm:ss`
- Turn-by-turn instructies uit de JSON gehaald en overzichtelijk afgedrukt
- Ondersteuning toegevoegd voor verschillende **vehicle profiles**:
  - `car`
  - `bike`
  - `foot`

**Resultaat:**  
Het script voert correcte routing-requests uit naar de GraphHopper API.  
De gebruiker kan in de terminal:

- een voertuigprofiel kiezen (car/bike/foot)
- een vertrek- en eindlocatie ingeven
- de totale afstand en reistijd zien
- alle turn-by-turn instructies volgen

Dit experiment toont aan dat ik een externe REST-API kan integreren in een Python applicatie, inclusief error handling en JSON-processing.

**Bestanden:**

- `graphhopper_parse-json_1.py`
- `graphhopper_parse-json_2.py`
- `graphhopper_parse-json_3.py`
- `graphhopper_parse-json_4.py`
- `graphhopper_parse-json_5.py`
- `graphhopper_parse-json_6.py`
- `graphhopper_parse-json_7.py`  *(final version)*

