# Dc1 – Docker Containers Run & Management

## Doel
Dit experiment toont dat ik Docker containers kan:
- starten (foreground en background)
- inspecteren (ps, logs)
- stoppen
- verwijderen (cleanup)

Hiervoor gebruik ik mijn eigen images:
- `di2-hello-app`
- `di3-env-message-app`

## Script
Het script `dc1_run_containers.sh` voert de volgende stappen uit:

1. Toont de images:
   ```bash
   docker images di2-hello-app di3-env-message-app
2. Start een korte foreground container:

docker run --rm di2-hello-app


3. Start een named container in de achtergrond met environment variables:

docker run -d --name dc1-di3 \
  -e NAME="Cindy" \
  -e ENVIRONMENT="test" \
  di3-env-message-app

4. Toont draaiende containers:

docker ps


5. Toont logs:

docker logs dc1-di3

6. Stopt de container:

docker stop dc1-di3

7. Verwijdert de container:

docker rm dc1-di3

## Link met DevOps
In DevOps is container management essentieel:

- services starten/stoppen

- logs bekijken voor troubleshooting

- resources opruimen

- werken met named containers en environment variables
