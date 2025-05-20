from flask import Flask, jsonify, request, abort
from blueprints.items import bp as items_bp

app = Flask(__name__)
app.register_blueprint(items_bp)

@app.route('/')
def index():
    return 'Hello, Flask'

@app.route('/ping')
def ping():
    data = {'message': 'pong'}
    return jsonify(data), 200


# 7. Error handlers personalizados
@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': str(e)}), 404

@app.errorhandler(400)
def bad_request(e):
    return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)