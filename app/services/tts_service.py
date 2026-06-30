import subprocess
import uuid
import os
import re

PIPER_EXE = r"D:\piper\piper.exe"
MODEL = r"D:\piper\models\en_US-lessac-medium.onnx"

OUTPUT_FOLDER = "static/audio"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def remove_emojis(text: str) -> str:
    # Remove characters outside the basic multilingual plane (most emojis)
    return re.sub(r"[^\u0000-\uFFFF]+", "", text)


def generate_voice(text: str):

    # Remove emojis before sending to Piper
    text = remove_emojis(text)

    filename = f"{uuid.uuid4()}.wav"

    output_path = os.path.join(OUTPUT_FOLDER, filename)

    subprocess.run(
        [
            PIPER_EXE,
            "-m",
            MODEL,
            "-f",
            output_path,
        ],
        input=text,
        text=True,
        encoding="utf-8",
        check=True,
    )

    return filename