from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="TAKE52")

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static",
)

templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "title": "TAKE52 — видеосъёмка в Нижнем Новгороде",
        },
    )
@app.get("/yandex_5ce173d08fc739d.html", response_class=HTMLResponse)
async def yandex_verification():
    return """
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    </head>
    <body>Verification: 5ce173d08fc739d</body>
</html>
"""
