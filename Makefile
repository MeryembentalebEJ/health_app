init:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

run:
	@echo "Running the Flask app..."
	python app.py

test:
	@echo "Running tests..."
	python -m unittest discover -s tests

build:
	@echo "Building the Docker image..."
	docker build -t health-calculator .

clean:
	@echo "Cleaning up..."
	rm -rf __pycache__
