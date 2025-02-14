init:
	@echo "📦 Installing dependencies..."
	python -m venv venv && \
	pip install -r requirements.txt

run:
	@echo "🚀 Running the Flask app..."
	
	python app.py

test:
	@echo "🧪 Running tests..."
	python -m unittest discover -s tests

deploy:
	@echo "🚀 Deploying to Azure..."
	az webapp up --name stay-healthy --resource-group healthAppDevops --runtime "PYTHON:3.12" --os-type Linux
