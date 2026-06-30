import glob
import os

from app.ai import generate_script
from app.tts import generate_voice
from app.scene_splitter import split_into_scenes
from app.services.image_service import generate_scene_images
from app.services.video_service import create_video


def generate_complete_video(
    prompt: str,
    style: str,
    duration: str,
    language: str,
):
    print("=" * 50)
    print("SHORTFORGE AI PIPELINE STARTED")
    print("=" * 50)

    # Step 1
    print("Generating script...")
    script = generate_script(
        prompt,
        style,
        duration,
        language,
    )

    # Step 2
    print("Splitting scenes...")
    scenes = split_into_scenes(script)

    # Step 3
    print("Generating images...")
    images = generate_scene_images(scenes)

    # Step 4
    print("Generating voice...")
    voice_file = generate_voice(script)

    audio_path = os.path.join(
        "static",
        "audio",
        voice_file,
    )

    # Step 5
    print("Creating video...")
    video = create_video(
        images,
        audio_path,
    )

    print("=" * 50)
    print("PIPELINE COMPLETE")
    print("=" * 50)

    return {
        "script": script,
        "video": video,
        "audio": audio_path,
        "images": images,
    }