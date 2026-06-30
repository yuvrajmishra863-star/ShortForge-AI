import os
import json
import shutil
import time
from datetime import datetime

from app.ai import generate_script
from app.tts import generate_voice
from app.scene_splitter import split_into_scenes
from app.services.image_service import generate_scene_images
from app.services.video_service import create_video

OUTPUT_FOLDER = "outputs"


def generate_complete_video(
    prompt: str,
    style: str,
    duration: str,
    language: str,
):

    start_time = time.time()

    # -------------------------------
    # Create Project Folder
    # -------------------------------

    project_id = datetime.now().strftime("%Y%m%d_%H%M%S")

    project_folder = os.path.join(
        OUTPUT_FOLDER,
        project_id
    )

    images_folder = os.path.join(
        project_folder,
        "images"
    )

    os.makedirs(images_folder, exist_ok=True)

    print("=" * 60)
    print("🚀 SHORTFORGE AI")
    print("=" * 60)

    # -------------------------------
    # Script
    # -------------------------------

    print("Generating Script...")

    script = generate_script(
        prompt,
        style,
        duration,
        language
    )

    script_path = os.path.join(
        project_folder,
        "script.txt"
    )

    with open(
        script_path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(script)

    # -------------------------------
    # Scenes
    # -------------------------------

    print("Splitting Scenes...")

    scenes = split_into_scenes(script)

    # -------------------------------
    # Images
    # -------------------------------

    print("Generating Images...")

    generated_images = generate_scene_images(scenes)

    project_images = []

    for image in generated_images:

        filename = os.path.basename(image)

        destination = os.path.join(
            images_folder,
            filename
        )

        shutil.copy2(
            image,
            destination
        )

        project_images.append(destination)

    # -------------------------------
    # Voice
    # -------------------------------

    print("Generating Voice...")

    voice_filename = generate_voice(script)

    source_voice = os.path.join(
        "static",
        "audio",
        voice_filename
    )

    destination_voice = os.path.join(
        project_folder,
        "voice.wav"
    )

    shutil.copy2(
        source_voice,
        destination_voice
    )

    # -------------------------------
    # Video
    # -------------------------------

    print("Creating Video...")

    temp_video = create_video(
        project_images,
        destination_voice
    )

    final_video = os.path.join(
        project_folder,
        "video.mp4"
    )

    shutil.copy2(
        temp_video,
        final_video
    )

    # -------------------------------
    # Metadata
    # -------------------------------

    generation_time = round(
        time.time() - start_time,
        2
    )

    metadata = {

        "project": project_id,

        "prompt": prompt,

        "style": style,

        "duration": duration,

        "language": language,

        "images": len(project_images),

        "generation_time": generation_time,

        "created_at": datetime.now().strftime(
            "%d %B %Y %I:%M:%S %p"
        )

    }

    with open(

        os.path.join(
            project_folder,
            "project.json"
        ),

        "w",

        encoding="utf-8"

    ) as f:

        json.dump(
            metadata,
            f,
            indent=4
        )

    print("=" * 60)
    print("✅ PROJECT COMPLETED")
    print(f"Project : {project_id}")
    print(f"Time    : {generation_time} sec")
    print("=" * 60)

    return {

        "project": project_id,

        "script": script,

        "video": final_video,

        "audio": destination_voice,

        "images": project_images

    }