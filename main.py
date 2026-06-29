from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from app.ai import generate_script

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>ShortForge AI</title>
    </head>
    <body style="font-family:Arial;text-align:center;margin-top:60px;">

        <h1>🎬 ShortForge AI</h1>

        <form action="/generate" method="post">

            <input
                type="text"
                name="prompt"
                placeholder="Enter your video topic"
                style="width:350px;height:35px;"
            >

            <br><br>

            <button type="submit">
                Generate AI Script
            </button>

        </form>

    </body>
    </html>
    """


@app.post("/generate", response_class=HTMLResponse)
def generate(prompt: str = Form(...)):

    script = generate_script(prompt)

    return f"""
    <html>

    <body style="font-family:Arial;margin:40px;">

        <h1>🎬 AI Generated Script</h1>

        <h3>Topic:</h3>

        <p>{prompt}</p>

        <hr>

        <pre style="white-space:pre-wrap;font-size:18px;">
{script}
        </pre>

        <br>

        <a href="/">⬅ Generate Another</a>

    </body>

    </html>
    """