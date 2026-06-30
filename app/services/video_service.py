from moviepy import ImageClip, AudioFileClip, concatenate_videoclips
import os

OUTPUT_FOLDER = "outputs/videos"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def create_video(images, audio_path):

    audio = AudioFileClip(audio_path)

    duration = audio.duration / len(images)

    clips = []

    for image in images:

        clip = (
            ImageClip(image)
            .resized(height=1920)
            .with_duration(duration)
        )

        clips.append(clip)

    final_video = concatenate_videoclips(
        clips,
        method="compose"
    )

    final_video = final_video.with_audio(audio)

    output = os.path.join(
        OUTPUT_FOLDER,
        "final_video.mp4"
    )

    final_video.write_videofile(
        output,
        fps=30,
        codec="libx264",
        audio_codec="aac"
    )

    return output