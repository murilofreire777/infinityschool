from flask import Blueprint, request, jsonify, abort

bp = Blueprint('items', __name__, url_prefix='/items')


items = [
    {'id': 1, 'name': 'Apple', 'price': 0.5},
    {'id': 2, 'name': 'Banana', 'price': 0.3}
]

def find_item(item_id):
    """Busca um item pelo ID, retornando None se não existir."""
    return next((item for item in items if item['id'] == item_id), None)


# 2. GET /items: retorna toda a lista
@bp.route('', methods=['GET'])
def get_items():
    return jsonify(items), 200

# 3. GET /items/: retorna um único item
@bp.route('/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = find_item(item_id)
    if not item:
        abort(404, description='Item não encontrado')
    return jsonify(item), 200

# 4. POST /items: cria um novo item
@bp.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    # Validação básica
    if not data or 'name' not in data or 'price' not in data:
        abort(400, description='Dados inválidos')
    new_id = max(item['id'] for item in items) + 1
    item = {'id': new_id, 'name': data['name'], 'price': data['price']}
    items.append(item)
    return jsonify(item), 201

# 5. PUT /items/: atualiza um item existente
@bp.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = find_item(item_id)
    if not item:
        abort(404, description='Item não encontrado')
    data = request.get_json()
    # Atualiza somente campos informados
    for key in ('name', 'price'):
        if key in data:
            item[key] = data[key]
    return jsonify(item), 200

# 6. DELETE /items/: remove um item
@bp.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = find_item(item_id)
    if not item:
        abort(404, description='Item não encontrado')
    items.remove(item)
    return '', 204

