# Pv2 – Python Virtual Environment Deployment

Dit experiment toont hoe een Python script in een geïsoleerde virtual environment wordt uitgevoerd.

## Run

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python pv1_http_requests.py
deactivate

## Voordeel

- dependency isolation

- reproducibility

- geen conflicts met system python

## Understanding – Virtual Environment (venv)

Zonder venv delen applicaties dezelfde Python packages, wat versieconflicten veroorzaakt.

Een virtual environment is een geïsoleerde Python installatie per project.

DevOps gebruikt venv zodat code reproduceerbaar kan gedeployed worden.
