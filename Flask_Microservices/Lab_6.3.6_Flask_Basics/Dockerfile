# 1. Basisimage met Python
FROM python:3.9-slim

# 2. Werkmap in de container
WORKDIR /app

# minder gedoe: eerst dependencies
COPY requirements.txt .

# 3. Installeer Flask 
# rustiger pip (minder threads / minder extra's)
RUN pip install --no-cache-dir --progress-bar off -r requirements.txt

# 4. Kopieer onze Flask-app naar de container
COPY app.py .

# 5. Poort 5000 openzetten
EXPOSE 5000

# 6. Start de Flask-app
CMD ["python", "app.py"]
