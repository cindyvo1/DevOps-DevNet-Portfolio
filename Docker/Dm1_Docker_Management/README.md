# Dm1 – Docker Management Experiment

##  Doel
In dit experiment toon ik dat ik Docker resources kan **beheren en opruimen**:
- images bekijken
- containers bekijken (ook gestopte)
- disk-usage analyseren
- gestopte containers opruimen
- dangling images opruimen

Dit hoort bij **Dm1 – Docker management-experiment**.

---

##  Bestanden
- `dm1_docker_management.sh` – script dat alle commando’s demonstreert

---

##  Wat doet het script?

1. **Images tonen**
   ```bash
   docker images

Laat alle lokale images zien (repository, tag, image ID, size).

2. Containers tonen (ook gestopte)

docker ps -a


Toont:

- draaiende containers

- gestopte containers

- namen, image, status

3. Disk usage bekijken

docker system df


Geeft overzicht:

- hoeveel ruimte images gebruiken

- hoeveel containers

- hoeveel volumes

4. Gestopte containers opruimen

docker container prune -f


Verwijdert ALLE gestopte containers.
(Met -f wordt de bevestigingsvraag automatisch met “yes” beantwoord.)

5. Dangling images opruimen

docker image prune -f


Verwijdert images zonder tag die niet meer gebruikt worden
(typisch oude build-lagen).

6. Situatie na cleanup tonen

docker images
docker ps -a

Hiermee kan je het verschil vóór en na de cleanup laten zien.

## Verschil tussen Dc1 en Dm1

Dc1 focust op: containers starten, logs, stoppen, verwijderen (runtime).

Dm1 focust op: beheer & cleanup van:

- gestopte containers

- dangling images

- disk usage

Samen tonen ze:

- dat ik containers kan runnen (Dc1)

- en Docker resources kan onderhouden (Dm1)

## Link met DevOps

In een DevOps-context is Docker management belangrijk omdat:

- oudere containers en images disk-space opeten

- CI/CD pipelines continu nieuwe images bouwen

- regelmatig prune nodig is om de omgeving proper te houden

- je moet begrijpen wat je weggooit (alleen gestopte containers / dangling images)

Dit experiment toont dat ik:

- Docker status kan inspecteren

- gerichte cleanup kan doen

- kan uitleggen wat de impact is van elk commando
