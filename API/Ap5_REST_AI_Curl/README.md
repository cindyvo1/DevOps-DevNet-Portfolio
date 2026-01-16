# Ap5 – REST “AI” experiment met curl

Doel: met `curl` een externe REST-API aanspreken die slimme woord-suggesties geeft
(soort mini taal-AI).

API: https://api.datamuse.com/  
- `/words?ml=<woord>&max=5`  → woorden met gelijkaardige betekenis  
- `/words?rel_rhy=<woord>&max=5` → woorden die rijmen

## Bestanden

- `ap5_rest_ai_curl.sh` – bash-script dat twee GET-requests doet met `curl`.

## Gebruik

```bash
./ap5_rest_ai_curl.sh           # gebruikt standaard het woord "network"
./ap5_rest_ai_curl.sh devops    # ander woord
