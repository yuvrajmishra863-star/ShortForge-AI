import re


def split_into_scenes(script: str, max_sentences: int = 2):
    """
    Splits a script into scenes.

    Every scene contains up to max_sentences sentences.
    """

    script = script.replace("\n", " ")

    sentences = re.split(r'(?<=[.!?])\s+', script)

    sentences = [s.strip() for s in sentences if s.strip()]

    scenes = []

    current_scene = []

    for sentence in sentences:

        current_scene.append(sentence)

        if len(current_scene) >= max_sentences:

            scenes.append(" ".join(current_scene))

            current_scene = []

    if current_scene:

        scenes.append(" ".join(current_scene))

    return scenes