# Begrip – Flask Microservice Basics

## Wat is Flask?
Flask is een lichtgewicht Python webframework waarmee je snel
een webservice of API kan bouwen.

## Wat doet deze applicatie?
Deze applicatie start een lokale webserver die luistert op poort 5000
en een HTTP-response terugstuurt wanneer de root-URL (/) wordt bezocht.

## Uitleg van de code

### Flask app initialiseren
`app = Flask(__name__)`
→ Dit maakt een Flask-applicatie aan.

### Route definiëren
`@app.route("/")`
→ Dit bepaalt welke URL wordt gekoppeld aan een functie.

### Response terugsturen
`return "Hello, this is my first Flask microservice!"`
→ Dit is de HTTP-response die de client ontvangt.

### Applicatie starten
`app.run(host="0.0.0.0", port=5000)`
→ Start de webserver zodat deze bereikbaar is via localhost.

## Wat heb ik hieruit geleerd?
- Wat een microservice is
- Hoe een HTTP-request en response werken
- Hoe Flask gebruikt wordt om API-endpoints te maken

## Wat betekent http://localhost:5000?

- **http**  
  Het protocol dat gebruikt wordt voor communicatie tussen client en server.

- **localhost**  
  Verwijst naar mijn eigen computer (127.0.0.1).  
  Dit betekent dat de Flask-app lokaal draait in de DEVASC VM.

- **5000**  
  De poort waarop de Flask-app luistert.  
  Flask gebruikt standaard poort 5000 voor webapplicaties.

Wanneer ik in de browser of met curl naar  
`http://localhost:5000` ga, stuur ik een HTTP-request
naar mijn eigen Flask microservice.

De Flask-app verwerkt dit request en stuurt een HTTP-response terug.

## Link met DevOps
Deze microservice kan later:
- in een Docker container geplaatst worden
- automatisch gebouwd worden via Jenkins
- deel uitmaken van een CI/CD pipeline

---

## Docker – uitbreiding op dit lab

### Waarom Docker gebruiken voor deze Flask microservice?
Docker zorgt ervoor dat deze Flask microservice
overal op dezelfde manier kan draaien,
ongeacht het besturingssysteem of de omgeving.

### Wat heb ik gedaan met Docker?
- Een Dockerfile aangemaakt voor deze Flask-app
- Een Docker image gebouwd met `docker build`
- Een container gestart met `docker run`
- De applicatie getest via http://localhost:5000

### Wat is het verschil tussen Flask lokaal en in Docker?
- Lokaal draait Flask rechtstreeks op de VM
- In Docker draait Flask in een container met een eigen omgeving

De functionaliteit is hetzelfde,
maar Docker maakt de applicatie reproduceerbaar en portable.

### Wat betekent poort-mapping (`-p 5000:5000`)?
Poort 5000 van de container wordt gekoppeld
aan poort 5000 van de host (DEVASC VM),
waardoor de applicatie bereikbaar is via localhost.

### Link met DevOps
Door Flask te combineren met Docker,
kan deze microservice eenvoudig geïntegreerd worden
in een CI/CD pipeline (bijvoorbeeld Jenkins).

