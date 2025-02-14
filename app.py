from flask import Flask
from app import create_app

app = create_app()

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))  # ✅ Azure utilise souvent le port 8000
    app.run(host="0.0.0.0", port=port)
