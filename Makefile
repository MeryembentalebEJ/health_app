# Définition des variables
PYTHON=python
VENV_DIR=venv
ACTIVATE=. $(VENV_DIR)/bin/activate

# Initialisation: Création de l'environnement virtuel et installation des dépendances
init:
	@echo "Creating virtual environment and installing dependencies..."
	$(PYTHON) -m venv $(VENV_DIR)
	$(ACTIVATE) && pip install -r requirements.txt

# Lancer l'application Flask
run: init
	@echo "Running the Flask app..."
	$(ACTIVATE) && python app.py

# Exécuter les tests
test: init
	@echo "Running tests..."
	$(ACTIVATE) && python -m unittest discover -s tests

# Construire l'image Docker
build:
	@echo "Building the Docker image..."
	docker build -t health-app .

# Nettoyer les fichiers temporaires
clean:
	@echo "Cleaning up..."
	rm -rf __pycache__ $(VENV_DIR)
