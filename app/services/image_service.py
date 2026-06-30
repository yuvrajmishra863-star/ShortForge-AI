import os
import uuid
import requests
from urllib.parse import quote

OUTPUT_FOLDER = "outputs/images"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def generate_image(prompt: str):

    filename = f"{uuid.uuid4()}.png"

    filepath = os.path.join(OUTPUT_FOLDER, filename)

    url = (
        "https://image.pollinations.ai/prompt/"
        + quote(prompt)
        + "?width=1080&height=1920&nologo=true"
    )

    response = requests.get(url, timeout=120)

    response.raise_for_status()

    with open(filepath, "wb") as f:
        f.write(response.content)

    return filepath


def generate_scene_images(scenes):

    images = []

    for i, scene in enumerate(scenes, start=1):

        print(f"Generating Image {i}/{len(scenes)}...")

        prompt = (
            f"Cinematic, ultra realistic, highly detailed, "
            f"vertical 9:16, {scene}"
        )

        image = generate_image(prompt)

        images.append(image)

    return images