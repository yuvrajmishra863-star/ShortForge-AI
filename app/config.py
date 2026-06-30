from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --------------------------------------------------
# Project Information
# --------------------------------------------------

APP_NAME = "ShortForge AI"
VERSION = "1.0.0"
AUTHOR = "Yuvraj Mishra"

# --------------------------------------------------
# Base Directories
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_DIR = BASE_DIR / "static"

TEMPLATE_DIR = BASE_DIR / "templates"

OUTPUT_DIR = BASE_DIR / "outputs"

AUDIO_DIR = OUTPUT_DIR / "audio"

IMAGE_DIR = OUTPUT_DIR / "images"

VIDEO_DIR = OUTPUT_DIR / "videos"

SCRIPT_DIR = OUTPUT_DIR / "scripts"

UPLOAD_DIR = BASE_DIR / "uploads"

MODEL_DIR = BASE_DIR / "models"

# --------------------------------------------------
# Create folders automatically
# --------------------------------------------------

for folder in [
    OUTPUT_DIR,
    AUDIO_DIR,
    IMAGE_DIR,
    VIDEO_DIR,
    SCRIPT_DIR,
    UPLOAD_DIR,
    MODEL_DIR,
]:
    folder.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# Environment Variables
# --------------------------------------------------

HF_TOKEN = os.getenv("HF_TOKEN", "")

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY", "")

OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434/api/generate"
)

# --------------------------------------------------
# Piper Configuration
# --------------------------------------------------

PIPER_EXE = r"D:\piper\piper.exe"

PIPER_MODEL = r"D:\piper\models\en_US-lessac-medium.onnx"

# --------------------------------------------------
# Video Configuration
# --------------------------------------------------

VIDEO_WIDTH = 1080

VIDEO_HEIGHT = 1920

FPS = 30