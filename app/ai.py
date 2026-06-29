import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_script(prompt):
    payload = {
        "model": "gemma3:1b",
        "prompt": f"Write a 30-second YouTube Shorts script about: {prompt}",
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    data = response.json()
    return data["response"]