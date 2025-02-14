from flask import Blueprint, request, jsonify
from app.health_utils import calculate_bmi, calculate_bmr

api_bp = Blueprint('api', __name__)

@api_bp.route('/bmi', methods=['POST'])
def bmi():
    try:
        data = request.get_json()
        weight = data.get("weight")
        height = data.get("height")
        if not weight or not height:
            return jsonify({"error": "Missing parameters"}), 400
        return jsonify({"bmi": calculate_bmi(height, weight)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_bp.route('/bmr', methods=['POST'])
def bmr():
    try:
        data = request.get_json()
        weight = data.get("weight")
        height = data.get("height")
        age = data.get("age")
        gender = data.get("gender")
        if not weight or not height or not age or not gender:
            return jsonify({"error": "Missing parameters"}), 400
        return jsonify({"bmr": calculate_bmr(height, weight, age, gender)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
