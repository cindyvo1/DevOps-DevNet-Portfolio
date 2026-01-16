# Di3 – Eigen Docker image 2 (met environment variables)
FROM python:3.9-slim

WORKDIR /app

COPY app.py /app/app.py

# Optioneel: standaard env vars instellen
ENV NAME="DevOps student" \
    ENVIRONMENT="local"

CMD ["python", "app.py"]
