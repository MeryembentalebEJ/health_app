# Image de base légère
FROM python:3.11-slim

# Définition du dossier de travail
WORKDIR /app

# Copie des fichiers sources
COPY . /app

# Installation des dépendances
RUN pip install --upgrade pip && pip install -r requirements.txt

# Exposition du port pour Flask
EXPOSE 5000

# Commande de lancement
CMD ["python", "app.py"]
