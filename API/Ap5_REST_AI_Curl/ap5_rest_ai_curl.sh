#!/bin/bash
# Ap5 - REST "AI" experiment met curl
# Gebruik: ./ap5_rest_ai_curl.sh [woord]

WORD="${1:-network}"   # standaard woord = "network" als je niks meegeeft

echo "== Similar words for: $WORD =="
curl -s "https://api.datamuse.com/words?ml=${WORD}&max=5"
echo
echo

echo "== Rhymes with: $WORD =="
curl -s "https://api.datamuse.com/words?rel_rhy=${WORD}&max=5"
echo
echo "Done."
