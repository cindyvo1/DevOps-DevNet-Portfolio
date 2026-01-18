# A2 – Eigen Ansible Playbook (Webserver)

## Doel
Met dit experiment toon ik hoe je met Ansible automatisch een webserver (nginx) kunt installeren en configureren op een Linux-server.

## Structuur
- `hosts.ini` – Ansible inventory met de *webservers* groep.
- `a2_webserver.yml` – hoofd-playbook dat nginx installeert, de webroot aanmaakt en een custom `index.html` plaatst.
- `files/index.html` – eenvoudige webpagina die door Ansible wordt gedeployed.

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
