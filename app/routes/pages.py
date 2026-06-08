from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.core.templates import templates


router = APIRouter(tags=["Pages"])


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "title": "TAKE52 — постановочное видео и визуальные истории",
            "version": "2",
        },
    )