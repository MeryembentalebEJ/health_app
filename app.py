from flask import Flask, send_from_directory
from app import create_app
import os

app = create_app()

# Assurer que Flask sert bien le frontend
@app.route('/')
def serve_frontend():
    return send_from_directory(os.path.abspath('frontend'), 'index.html')

# Assurer que Flask sert bien les fichiers statiques (CSS, JS)
@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory(os.path.abspath('frontend'), path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
