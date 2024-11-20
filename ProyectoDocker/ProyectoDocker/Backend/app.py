from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Datos simulados (inicialmente vacíos)
items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"}
]

# Obtener todos los items (Read)
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Crear un nuevo item (Create)
@app.route('/api/items', methods=['POST'])
def create_item():
    new_item = request.json
    new_item['id'] = len(items) + 1  # Asigna un ID único basado en el tamaño de la lista
    items.append(new_item)
    return jsonify(new_item), 201

# Actualizar un item existente (Update)
@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    updated_item = request.json
    for item in items:
        if item['id'] == item_id:
            item.update(updated_item)
            return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# Eliminar un item (Delete)
@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"message": "Item deleted"}), 200

# Ruta de prueba original
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'message': 'Hello from Flask!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
