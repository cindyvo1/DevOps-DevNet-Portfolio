# Di2 – Eigen Docker image experiment

## Doel
Een eigen Docker image maken op basis van `python:3.9-slim` en testen dat de container correct runt.

Het doel is inzicht te krijgen in:
- de structuur van een Dockerfile
- hoe images gebouwd worden
- hoe containers de image uitvoeren
- het verschil tussen image en container
- de basis workflow van `build → run`

## Bestanden
- `app.py` – klein Python script dat een boodschap print
- `Dockerfile` – build instructies voor de Docker image

## Image bouwen
```bash
docker build -t di2-hello-app .

## 🧱 De applicatie (app.py)
Het script print een simpele boodschap, zodat we duidelijk kunnen zien dat de container de code uitvoert:

```python
print("===================================")
print("  DI2 – Eigen Docker image test  ")
print("  Hello from inside the container ")
print("===================================")

