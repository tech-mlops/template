from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
]


@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "service": "example-api", "version": "v1"}), 200


@app.route("/api/v1/users", methods=["GET"])
def get_users():
    """Get all users"""
    return jsonify({"users": users}), 200


@app.route("/api/v1/users", methods=["POST"])
def create_user():
    """Create a new user"""
    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "name and email are required"}), 400

    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "email": data["email"]
    }
    users.append(new_user)
    return jsonify({"user": new_user}), 201


@app.route("/api/v1/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    """Get user by ID"""
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"user": user}), 200


@app.route("/api/v1/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    """Update user by ID"""
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    if "name" in data:
        user["name"] = data["name"]
    if "email" in data:
        user["email"] = data["email"]

    return jsonify({"user": user}), 200


@app.route("/api/v1/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """Delete user by ID"""
    global users
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404

    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "User deleted successfully"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
