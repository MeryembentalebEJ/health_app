init:
	@echo "📦 Installing dependencies..."
	python -m venv venv && \
	source venv/bin/activate && \
	pip install -r requirements.txt

run:
	@echo "🚀 Running the Flask app locally..."
	source venv/bin/activate && \
	python app.py  # Garder cette version pour les tests en local

run-prod:
	@echo "🚀 Running the Flask app in production with Gunicorn..."
	source venv/bin/activate && \
	gunicorn -w 4 -b 0.0.0.0:8000 app:app

test:
	@echo "🧪 Running tests..."
	source venv/bin/activate && \
	python -m unittest discover -s tests

deploy:
	@echo "🚀 Deploying to Azure..."
	az webapp up --name stay-healthy --resource-group healthAppDevops --runtime "PYTHON:3.12" --os-type Linux
