from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, FileResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.ai import generate_script
from app.tts import generate_voice

# Database
from app.database.db import Base, engine
from app.models.project import Project

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Static Files
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@app.post("/generate", response_class=HTMLResponse)
async def generate(
    request: Request,
    prompt: str = Form(...),
    style: str = Form(...),
    duration: str = Form(...),
    language: str = Form(...)
):
    script = generate_script(
        prompt,
        style,
        duration,
        language
    )

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "prompt": prompt,
            "style": style,
            "duration": duration,
            "language": language,
            "script": script
        }
    )


@app.post("/voice")
async def voice(script: str = Form(...)):
    try:
        filename = generate_voice(script)

        return FileResponse(
            path=f"static/audio/{filename}",
            media_type="audio/wav",
            filename="voice.wav"
        )

    except Exception as e:
        import traceback

        traceback.print_exc()

        return PlainTextResponse(
            f"ERROR:\n\n{str(e)}",
            status_code=500
        )