from flask import Flask, request, jsonify, render_template
import requests
import json

app = Flask(__name__)

OLLAMA_SERVER_URL = 'http://127.0.0.1:11434/api'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/models', methods=['GET'])
def get_models():
    try:
        response = requests.get(f'{OLLAMA_SERVER_URL}/tags')  # Changed from /models to /tags
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching models from Ollama server: {e}")
        return jsonify({'error': 'Failed to fetch models from Ollama server'}), 500

    models_data = response.json()
    # Extract just the model names
    models = [model.get('name') for model in models_data.get('models', [])]
    return jsonify(models)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    model_name = request.json.get('model')
    if not user_message or not model_name:
        return jsonify({'error': 'No message or model provided'}), 400

    try:
        # Use stream=False to get the complete response at once
        response = requests.post(
            f'{OLLAMA_SERVER_URL}/generate', 
            json={
                'model': model_name,
                'prompt': user_message,
                'stream': False
            }
        )
        response.raise_for_status()
        ollama_response = response.json()
        response_text = ollama_response.get('response', 'No response')
        return jsonify({'response': response_text})
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with Ollama server: {e}")
        return jsonify({'error': f'Failed to communicate with Ollama server: {str(e)}'}), 500
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON from Ollama server: {e}")
        return jsonify({'error': f'Invalid response from Ollama server: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
