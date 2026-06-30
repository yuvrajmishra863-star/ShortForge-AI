from app.scene_splitter import split_into_scenes
from app.services.image_service import generate_scene_images

script = """
The Taj Mahal is one of the Seven Wonders of the World.
It was built by Mughal Emperor Shah Jahan.
Millions of tourists visit it every year.
It is made from white marble.
It symbolizes eternal love.
"""

scenes = split_into_scenes(script)

print("=" * 50)
print("Scenes Generated")
print("=" * 50)

for scene in scenes:
    print(scene)
    print()

print("=" * 50)

images = generate_scene_images(scenes)

print("Generated Images:")

for img in images:
    print(img)