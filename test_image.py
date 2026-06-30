from app.services.image_service import generate_image

image = generate_image(
    "A futuristic cyberpunk city at sunset, ultra realistic, cinematic lighting, 9:16"
)

print("=" * 50)
print("IMAGE GENERATED SUCCESSFULLY")
print(image)
print("=" * 50)