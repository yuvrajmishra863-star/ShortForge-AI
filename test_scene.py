from app.scene_splitter import split_into_scenes

script = """
The Taj Mahal is one of the most famous monuments in the world.
It was built by Shah Jahan.
Millions of tourists visit every year.
Its white marble changes color throughout the day.
It is considered a symbol of eternal love.
"""

scenes = split_into_scenes(script)

print("=" * 50)

for i, scene in enumerate(scenes, start=1):
    print(f"Scene {i}")
    print(scene)
    print("-" * 50)