import re

def split_into_scenes(script: str):
    """
    Split the generated AI script into scenes.
    Each non-empty paragraph becomes one scene.
    """

    scenes = [
        line.strip()
        for line in re.split(r"\n\s*\n", script)
        if line.strip()
    ]

    # If the AI returned everything in one paragraph,
    # split by sentence instead.
    if len(scenes) == 1:
        scenes = [
            sentence.strip()
            for sentence in re.split(r'(?<=[.!?])\s+', script)
            if sentence.strip()
        ]

    return scenes