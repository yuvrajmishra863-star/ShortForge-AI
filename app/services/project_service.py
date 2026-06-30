import os
from datetime import datetime

OUTPUT_FOLDER = "outputs"


def get_projects():
    """
    Returns all generated projects sorted newest first.
    """

    projects = []

    if not os.path.exists(OUTPUT_FOLDER):
        return projects

    folders = sorted(
        os.listdir(OUTPUT_FOLDER),
        reverse=True
    )

    for folder in folders:

        project_path = os.path.join(
            OUTPUT_FOLDER,
            folder
        )

        if not os.path.isdir(project_path):
            continue

        video_path = os.path.join(
            project_path,
            "video.mp4"
        )

        voice_path = os.path.join(
            project_path,
            "voice.wav"
        )

        script_path = os.path.join(
            project_path,
            "script.txt"
        )

        images_folder = os.path.join(
            project_path,
            "images"
        )

        image_count = 0

        if os.path.exists(images_folder):

            image_count = len([
                file
                for file in os.listdir(images_folder)
                if file.lower().endswith(
                    (".png", ".jpg", ".jpeg", ".webp")
                )
            ])

        created = datetime.fromtimestamp(
            os.path.getctime(project_path)
        )

        projects.append({

            "id": folder,

            "created": created.strftime(
                "%d %b %Y %I:%M %p"
            ),

            "video": (
                "/"
                + video_path.replace("\\", "/")
            ),

            "voice": (
                "/"
                + voice_path.replace("\\", "/")
            ),

            "script": (
                "/"
                + script_path.replace("\\", "/")
            ),

            "images": image_count

        })

    return projects