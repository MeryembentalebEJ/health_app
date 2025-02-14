from flask import Flask, request, jsonify
import logging
from health_utils import calculate_bmi, calculate_bmr

# Configuration du logger
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/bmi', methods=['POST'])
def calculate_bmi_api():
    """Endpoint pour calculer l'IMC (BMI)."""
    data = request.get_json()

    if not data or 'height' not in data or 'weight' not in data:
        return jsonify({'error': 'Données incomplètes. Veuillez fournir la taille (height) et le poids (weight).'}), 400

    try:
        height = float(data['height'])
        weight = float(data['weight'])
        bmi_value = calculate_bmi(height, weight)
        return jsonify({'bmi': bmi_value}), 200
    except ValueError as e:
        return jsonify({'error': f"Valeur invalide : {str(e)}"}), 400

@app.route('/bmr', methods=['POST'])
def calculate_bmr_api():
    """Endpoint pour calculer le BMR."""
    data = request.get_json()
    required_keys = {'height', 'weight', 'age', 'gender'}

    if not data or not required_keys.issubset(data):
        return jsonify({'error': 'Données incomplètes. Veuillez fournir la taille (height), le poids (weight), l\'âge (age) et le genre (gender).'}), 400

    try:
        height = float(data['height'])
        weight = float(data['weight'])
        age = int(data['age'])
        gender = data['gender'].lower()

        bmr_value = calculate_bmr(height, weight, age, gender)
        return jsonify({'bmr': bmr_value}), 200
    except ValueError as e:
        return jsonify({'error': f"Valeur invalide : {str(e)}"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
