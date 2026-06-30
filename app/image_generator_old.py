import os
import uuid
import requests
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}


def generate_image(prompt):

    os.makedirs("outputs/images", exist_ok=True)

    filename = f"{uuid.uuid4()}.png"

    filepath = os.path.join("outputs/images", filename)

    response = requests.post(
        API_URL,
        headers=headers,
        json={
            "inputs": prompt
        },
        timeout=300
    )

    if response.status_code != 200:
        raise Exception(response.text)

    with open(filepath, "wb") as f:
        f.write(response.content)

    return filepath