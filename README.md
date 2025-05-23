# Ollama Chat UI

A super simple web interface for interacting with Ollama language models.

## Features

- Select from available models in your Ollama server
- Simple chat interface
- Responsive design

## Prerequisites

- Python 3.8+
- Docker (for running Ollama)
- Git

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/gmdeckard/chat-ui.git
cd chat-ui
```

### 2. Set up Python environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run Ollama with Docker

```bash
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

### 4. Pull a model in Ollama

```bash
# Pull a small model to start with
docker exec -it ollama ollama pull tinyllama
```

Other models you might want to try:
- `llama2`
- `mistral`
- `gemma`
- `phi`

### 5. Run the Chat UI

```bash
python app.py
```

The application will be available at: http://127.0.0.1:5000

## Usage

1. Open your browser and navigate to http://127.0.0.1:5000
2. Select a model from the dropdown
3. Type your message and press Enter or click Send
4. View the AI's response in the chat box


## Troubleshooting

- **No models showing up?** Make sure your Ollama server is running and has models installed.
- **Error connecting to Ollama server?** Check that Ollama is running on port 11434.
- **Getting JSON decode errors?** Ensure you're using a compatible version of Ollama.

## License

MIT
