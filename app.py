from flask import Flask, jsonify, request
from waitress import serve

app = Flask(__name__)

@app.route('/ping')
def home():
    return jsonify({"message": "Welcome to the Flask API!"})

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Guest')
    return jsonify({"message": f"Hello, {name}!"})

@app.route('/sum', methods=['POST'])
def calculate_sum():
    data = request.get_json()
    if not data or 'a' not in data or 'b' not in data:
        return jsonify({"error": "Please provide 'a' and 'b' values"}), 400
    return jsonify({"sum": data['a'] + data['b']})

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5050)
