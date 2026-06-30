import glob

from app.services.video_service import create_video

images = sorted(glob.glob("outputs/images/*.png"))

audio = sorted(glob.glob("static/audio/*.wav"))[-1]

video = create_video(images, audio)

print("=" * 50)
print("VIDEO CREATED")
print(video)
print("=" * 50)