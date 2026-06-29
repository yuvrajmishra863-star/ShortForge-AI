import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_script(prompt, style, duration, language):

    full_prompt = f"""
You are an expert YouTube Shorts writer.

Generate a {style} script.

Topic:
{prompt}

Language:
{language}

Video Length:
{duration}

Rules:

1. Start with a powerful hook.
2. Make it engaging.
3. Keep it suitable for YouTube Shorts.
4. Finish with a call to action.
5. Return only the script.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "gemma3:1b",
            "prompt": full_prompt,
            "stream": False
        }
    )

    response.raise_for_status()

    return response.json()["response"]