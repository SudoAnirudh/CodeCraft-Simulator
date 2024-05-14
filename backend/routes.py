from flask import Blueprint, request, jsonify
from models import db, User, Quest
import services

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = services.create_user(data['username'], data['email'])
    return jsonify(user)

@api_blueprint.route('/quest/<int:quest_id>', methods=['GET'])
def get_quest(quest_id):
    quest = Quest.query.get(quest_id)
    return jsonify(quest)

@api_blueprint.route('/submit_code', methods=['POST'])
def submit_code():
    data = request.get_json()
    result = services.run_code(data['user_id'], data['code'])
    return jsonify(result)
