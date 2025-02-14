init:
	@echo "📦 Installing dependencies..."
	python -m venv venv && \
	. venv/bin/activate && \
	pip install -r requirements.txt

run:
	@echo "🚀 Running the Flask app locally..."
	. venv/bin/activate && \
	python app.py

run-prod:
	@echo "🚀 Running the Flask app in production with Gunicorn..."
	. venv/bin/activate && \
	gunicorn -w 4 -b 0.0.0.0:5000 app:app
