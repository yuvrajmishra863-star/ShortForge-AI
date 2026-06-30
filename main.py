from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.database.db import Base, engine
from app.services.pipeline_service import generate_complete_video
from app.services.project_service import get_projects

app = FastAPI(
    title="ShortForge AI",
    version="1.0"
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Static folders
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/outputs", StaticFiles(directory="outputs"), name="outputs")

templates = Jinja2Templates(directory="templates")


# =====================================================
# HOME
# =====================================================

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    projects = get_projects()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "projects": projects
        }
    )


# =====================================================
# DASHBOARD
# =====================================================

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):

    projects = get_projects()

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "projects": projects
        }
    )


# =====================================================
# GENERATE
# =====================================================

@app.post("/generate", response_class=HTMLResponse)
async def generate(
    request: Request,
    prompt: str = Form(...),
    style: str = Form(...),
    duration: str = Form(...),
    language: str = Form(...)
):

    try:

        result = generate_complete_video(
            prompt=prompt,
            style=style,
            duration=duration,
            language=language
        )

        video_url = "/" + result["video"].replace("\\", "/")
        audio_url = "/" + result["audio"].replace("\\", "/")

        image_urls = [
            "/" + image.replace("\\", "/")
            for image in result["images"]
        ]

        return templates.TemplateResponse(
            request=request,
            name="result.html",
            context={
                "prompt": prompt,
                "style": style,
                "duration": duration,
                "language": language,
                "script": result["script"],
                "video_url": video_url,
                "audio_url": audio_url,
                "images": image_urls,
                "project": result["project"]
            }
        )

    except Exception as e:

        import traceback
        traceback.print_exc()

        return PlainTextResponse(
            str(e),
            status_code=500
        )