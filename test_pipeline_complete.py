from app.services.pipeline_service import generate_complete_video

result = generate_complete_video(
    prompt="The history of the Taj Mahal",
    style="Storytelling",
    duration="30 seconds",
    language="English",
)

print(result)
