import subprocess
import uuid
import os

PIPER_EXE = r"D:\piper\piper.exe"
MODEL = r"D:\piper\models\en_US-lessac-medium.onnx"

OUTPUT_FOLDER = "static/audio"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def generate_voice(text: str):

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
        check=True,
    )

    return filename