from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.ai import generate_script
from app.tts import generate_voice

app = FastAPI()

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
    filename = generate_voice(script)

    return FileResponse(
        path=f"static/audio/{filename}",
        media_type="audio/wav",
        filename="voice.wav"
    )