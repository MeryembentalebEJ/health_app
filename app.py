from flask import Flask, send_from_directory
from app import create_app
import os

app = create_app()

# Serve the frontend
@app.route('/')
def serve_frontend():
    return send_from_directory(os.path.join(os.getcwd(), 'frontend'), 'index.html')

# Serve static files
@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory(os.path.join(os.getcwd(), 'frontend'), path)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))  # ✅ Azure requires port 8000
    app.run(host='0.0.0.0', port=port, debug=True)
