from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Simulação de usuário em memória
users = {
    'murilo': {'password_hash': generate_password_hash('senha123')}
}

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = users.get(username)

    if not user or not check_password_hash(user['password_hash'], password):
        return jsonify({'msg': 'Usuário ou senha inválidos'}), 401

    access_token = create_access_token(identity=username)
    return jsonify({'access_token': access_token}), 200