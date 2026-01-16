#!/bin/bash
# Dc1 – Run containers experiment
# Vereist dat de images di2-hello-app en di3-env-message-app al bestaan.

echo "=== Dc1 – Docker containers run & manage ==="

echo
echo "1) Toon de relevante images:"
docker images di2-hello-app di3-env-message-app || echo "Images nog niet gebouwd"

echo
echo "2) Run een korte foreground container (di2-hello-app):"
docker run --rm di2-hello-app

echo
echo "3) Start di3-env-message-app in de achtergrond met naam en env vars:"
docker run -d \
  --name dc1-di3 \
  -e NAME="Cindy" \
  -e ENVIRONMENT="test" \
  di3-env-message-app

echo
echo "4) Toon draaiende containers:"
docker ps

echo
echo "5) Toon logs van dc1-di3:"
docker logs dc1-di3

echo
echo "6) Stop de container:"
docker stop dc1-di3

echo
echo "7) Verwijder de container (cleanup):"
docker rm dc1-di3 || echo "Container al verwijderd of met --rm gestart"

echo
echo "Dc1 experiment afgerond."
