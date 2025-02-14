IMAGE_NAME = health-calculator
PORT = 5000

.PHONY: init run test build clean

# Installation des dépendances
init:
	@echo "Installation des dépendances..."
	@pip install -r requirements.txt

# Lancement de l'application Flask
run:
	@echo "Démarrage de l'application Flask sur le port $(PORT)..."
	@python app.py

# Exécution des tests
test:
	@echo "Exécution des tests..."
	@pytest tests.py

# Création de l'image Docker
build:
	@echo "Construction de l'image Docker $(IMAGE_NAME)..."
	@docker build -t $(IMAGE_NAME) .

# Nettoyage des containers et des images
clean:
	@echo "Nettoyage des containers et des images Docker..."
	@docker rm -f $$(docker ps -a -q) || true
	@docker rmi -f $(IMAGE_NAME) || true
