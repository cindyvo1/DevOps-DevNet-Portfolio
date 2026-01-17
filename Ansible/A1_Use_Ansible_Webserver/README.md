# Lab A1 — Use Ansible to Automate Installing a Web Server

##  Doel
Automatiseren van de installatie en configuratie van Apache2 op een webserver via Ansible.

Uitgevoerd op de DEVASC VM van Cisco.

---

##  Gebruikte componenten

- Ansible Inventory (`hosts`)
- Ansible Config (`ansible.cfg`)
- Playbooks:
  - `test_apache_playbook.yaml`
  - `install_apache_playbook.yaml`
  - `install_apache_options_playbook.yaml`

---

## ️ Uitgevoerde taken

✔ SSH-toegang geconfigureerd  
✔ Ansible inventory aangemaakt  
✔ Ping / commando test via Ansible  
✔ Apache2 geïnstalleerd via playbook  
✔ Mod Rewrite geactiveerd  
✔ Apache opnieuw gestart via handler  
✔ Luisterpoort gewijzigd naar **8081**  
✔ VirtualHost aangepast  
✔ Apache werking geverifieerd

---

##  Bestanden

hosts → inventory
ansible.cfg → Ansible configuratie
test_apache_playbook.yaml → echo test playbook
install_apache_playbook.yaml → Apache installatie playbook
install_apache_options_playbook.yaml → Playbook met aangepaste poort

##  Test & Validatie

### 1. Ping test via Ansible

ansible webservers -m ping
 Resultaat: `pong`

### 2. Apache status

sudo systemctl status apache2
 Resultaat: `active (running)`

### 3. Poortconfiguratie

`/etc/apache2/ports.conf` → `Listen 8081`  
`/etc/apache2/sites-available/000-default.conf` → `<VirtualHost *:8081>`

### 4. Browser test

http://192.0.2.3:8081
 Resultaat: "Apache2 Ubuntu Default Page"

## ✔ Conclusie

De installatie van Apache2 is volledig geautomatiseerd via Ansible.  
Het aanpassen van configuratiebestanden en herstarten van services is gescript en reproduceerbaar.

Het lab is succesvol afgerond.
