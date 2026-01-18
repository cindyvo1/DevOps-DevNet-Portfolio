# A2 – Eigen Ansible Playbook (Webserver)

## Doel
Met dit experiment toon ik hoe je met Ansible automatisch een webserver (nginx) kunt installeren en configureren op een Linux-server.

## Structuur
- `hosts.ini` – Ansible inventory met de groep **webservers** (hier: localhost).
- `a2_webserver.yml` – hoofd-playbook dat:
  - de apt-cache bijwerkt,
  - nginx installeert,
  - de webroot controleert/aanmaakt,
  - een custom `index.html` kopieert,
  - en de nginx-service start en enabled.
- `files/index.html` – eenvoudige webpagina die via Ansible wordt gedeployed.

## Hoe uit te voeren

1. Ga naar de map:

   ```bash
   cd Ansible/A2_Webserver_Playbook
2. Run het playbook:

ansible-playbook -i hosts.ini a2_webserver.yml


3. Surf naar http://localhost in de browser van de VM.

4. Je zou de pagina "Welkom op mijn A2 webserver!" moeten zien.

## Wat dit demonstreert

Gebruik van een eigen Ansible-playbook (geen kopie van een lab).

Idempotente installatie en configuratie van een webserver.

Scheiding tussen inventory, playbook en statische bestanden.
