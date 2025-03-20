from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

OLLAMA_SERVER_URL = 'http://127.0.0.1:11434/api'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/models', methods=['GET'])
def get_models():
    try:
        response = requests.get(f'{OLLAMA_SERVER_URL}/models')
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching models from Ollama server: {e}")
        return jsonify({'error': 'Failed to fetch models from Ollama server'}), 500

    models = response.json()
    return jsonify(models)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    model_name = request.json.get('model')
    if not user_message or not model_name:
        return jsonify({'error': 'No message or model provided'}), 400

    try:
        response = requests.post(f'{OLLAMA_SERVER_URL}/chat', json={'message': user_message, 'model': model_name})
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with Ollama server: {e}")
        return jsonify({'error': 'Failed to communicate with Ollama server'}), 500

    ollama_response = response.json()
    return jsonify({'response': ollama_response})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
