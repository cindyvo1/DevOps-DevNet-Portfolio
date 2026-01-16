#!/bin/bash
# Dm1 – Docker management experiment
# Doel: tonen hoe je images en containers beheert en opruimt.

echo "=== Dm1 – Docker Management ==="

echo
echo "1) Toon alle images (docker images):"
docker images
echo

echo "2) Toon alle containers, ook gestopte (docker ps -a):"
docker ps -a
echo

echo "3) Toon Docker disk usage (docker system df):"
docker system df
echo

echo "4) Verwijder alle gestopte containers (docker container prune -f):"
docker container prune -f
echo

echo "5) Verwijder dangling images (docker image prune -f):"
docker image prune -f
echo

echo "6) Toon opnieuw images en containers na cleanup:"
docker images
echo
docker ps -a
echo

echo "Dm1 – management experiment afgerond."
