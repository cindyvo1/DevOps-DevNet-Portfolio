# A3 – Eigen Ansible Playbook (FTP-server)

## Doel
In dit experiment toon ik hoe je met Ansible automatisch een FTP-server (vsftpd) installeert en configureert op een Linux-machine.
De playbook maakt ook een upload directory en plaatst daar een welkomstbestand.

## Structuur
- `hosts.ini` – Ansible inventory met de groep **ftpservers** (hier: localhost).
- `a3_ftp_server.yml` – hoofd-playbook dat:
  - de apt-cache bijwerkt,
  - vsftpd installeert,
  - een upload directory `/srv/ftp/upload` aanmaakt,
  - een `welcome.txt` bestand kopieert,
  - en de vsftpd-service start en enabled.
- `files/welcome.txt` – tekstbestand dat in de FTP-upload directory wordt geplaatst.

## Hoe uit te voeren

1. Ga naar de map van dit experiment:

   ```bash
   cd Ansible/A3_FTP_Server

2.Voer het Ansible-playbook uit:

ansible-playbook -i hosts.ini a3_ftp_server.yml


3. Controleer of de service actief is:

systemctl status vsftpd


4. Controleer of de upload directory en het bestand bestaan:

ls -l /srv/ftp/upload

## Wat dit demonstreert

- Gebruik van een eigen Ansible-playbook voor een andere server dan A2 (hier: FTP-server vsftpd).

- Idempotente installatie en configuratie van een server.

- Gebruik van verschillende Ansible-modules: apt, file, copy, service.

- Duidelijke scheiding tussen inventory, playbook en statische bestanden.
