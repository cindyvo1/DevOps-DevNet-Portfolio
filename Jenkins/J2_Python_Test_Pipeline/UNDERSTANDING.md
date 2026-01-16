# Understanding – J2 Custom Jenkins Pipeline

## Wat doet deze pipeline?

- De pipeline is een voorbeeld van **Continuous Integration** voor een klein Python-project.
- Bij elke build worden automatisch:
  1. dependencies geïnstalleerd
  2. code gelint
  3. testen uitgevoerd

## Stages

1. **Install dependencies**
   - `pip install -r requirements.txt`
   - Installeert `pytest` en `flake8`.

2. **Lint**
   - `flake8 . || true`
   - Controleert code style.  
   - `|| true` zorgt ervoor dat de pipeline niet faalt op style-fouten (alleen waarschuwingen).

3. **Test**
   - `pytest`
   - Voert `test_calc.py` uit en controleert of de functie `add()` de juiste resultaten geeft.

## Waarom is dit CI?

- Developers pushen code naar GitHub.
- Jenkins haalt de code op via Git.
- De pipeline garandeert dat:
  - de code nog installeerbaar is
  - de style oké is
  - unit tests slagen

Dit voorkomt dat foute code in de main branch terechtkomt en verhoogt de kwaliteit.
