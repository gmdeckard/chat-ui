from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

OLLAMA_SERVER_URL = 'http://localhost:11434/api/chat'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    response = requests.post(OLLAMA_SERVER_URL, json={'message': user_message})
    if response.status_code != 200:
        return jsonify({'error': 'Failed to communicate with Ollama server'}), 500

    ollama_response = response.json()
    return jsonify({'response': ollama_response})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
