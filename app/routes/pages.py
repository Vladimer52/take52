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
    
@router.get("/vladimer52", response_class=HTMLResponse)
async def vladimer52(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="vladimer52.html",
        context={
            "title": "Vladimer52 — Владимир Макаров, видеограф TAKE52",
            "description": (
                "Vladimer52 — творческий ник Владимира Макарова, видеографа TAKE52 "
                "из Нижнего Новгорода. Видеосъёмка свадеб, корпоративов, выпускных, "
                "продуктовых роликов и визуальных историй."
            ),
            "version": "2",
        },
    )
