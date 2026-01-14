# Understanding – Jenkins CI Pipeline

## Wat lost Jenkins op?
Jenkins automatiseert build/test taken zodat code telkens getest wordt bij nieuwe commits.  
Dit verhoogt kwaliteit en reduceert manuele fouten.

## Concept: Continuous Integration (CI)
Continuous Integration betekent dat code van developers regelmatig samengebracht wordt in 1 centrale build/test flow.

Twee voordelen:
- fouten worden sneller gevonden
- code blijft consistent werkend

## Waarom GitHub + Jenkins?
GitHub = broncode → Jenkins = build/test automation  
Sync gebeurt automatisch via polling of webhooks.

## Wat doet onze pipeline?
Onze pipeline controleert enkel syntax/linting zodat foute Python code niet kan deployen.

Command:
python3 -m py_compile sample_app.py
Exit-codes:

0 → SUCCESS

≠0 → FAILURE

## Resultaat
Bij een geldige Flask-app kreeg de pipeline: Finished: SUCCESS

## Link met DevOps
CI zorgt ervoor dat fouten vroeg in de lifecycle worden gedetecteerd, vóór deployment.
Dit maakt samenwerking sneller en betrouwbaarder.
