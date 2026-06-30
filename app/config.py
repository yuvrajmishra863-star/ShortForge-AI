import os

# ----------------------------------------------------
# Project Paths
# ----------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STATIC_DIR = "static"

OUTPUT_DIR = "outputs"

AUDIO_DIR = os.path.join(
    STATIC_DIR,
    "audio"
)

IMAGE_DIR = os.path.join(
    OUTPUT_DIR,
    "images"
)

VIDEO_DIR = os.path.join(
    OUTPUT_DIR,
    "videos"
)

# ----------------------------------------------------
# Piper
# ----------------------------------------------------

PIPER_EXE = r"D:\piper\piper.exe"

PIPER_MODEL = r"D:\piper\models\en_US-lessac-medium.onnx"

# ----------------------------------------------------
# AI Image
# ----------------------------------------------------

POLLINATIONS_URL = "https://image.pollinations.ai/prompt/"

# ----------------------------------------------------
# Video
# ----------------------------------------------------

FPS = 30

WIDTH = 1080

HEIGHT = 1920

# ----------------------------------------------------
# Application
# ----------------------------------------------------

APP_NAME = "ShortForge AI"

VERSION = "1.0"

AUTHOR = "Yuvraj Mishra"