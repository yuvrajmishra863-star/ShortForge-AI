from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, FileResponse, PlainTextResponse
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
    try:
        print("=" * 50)
        print("VOICE ROUTE CALLED")
        print("Script Length:", len(script))

        filename = generate_voice(script)

        print("Generated File:", filename)

        file_path = f"static/audio/{filename}"

        print("File Path:", file_path)

        return FileResponse(
            path=file_path,
            media_type="audio/wav",
            filename="voice.wav"
        )

    except Exception as e:
        import traceback

        print("=" * 50)
        print("VOICE ERROR")
        traceback.print_exc()

        return PlainTextResponse(
            f"ERROR:\n\n{str(e)}",
            status_code=500
        )