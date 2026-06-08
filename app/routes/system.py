from fastapi import APIRouter
from fastapi.responses import FileResponse, HTMLResponse

from app.core.paths import STATIC_DIR


router = APIRouter(tags=["System"])


@router.api_route("/favicon.ico", methods=["GET", "HEAD"], include_in_schema=False)
async def favicon():
    return FileResponse(
        STATIC_DIR / "img" / "mascot.ico",
        media_type="image/vnd.microsoft.icon",
    )


@router.api_route("/robots.txt", methods=["GET", "HEAD"], include_in_schema=False)
async def robots_txt():
    return FileResponse(
        STATIC_DIR / "robots.txt",
        media_type="text/plain",
    )


@router.api_route("/sitemap.xml", methods=["GET", "HEAD"], include_in_schema=False)
async def sitemap_xml():
    return FileResponse(
        STATIC_DIR / "sitemap.xml",
        media_type="application/xml",
    )


@router.get("/yandex_5ce173d08f9c739d.html", response_class=HTMLResponse, include_in_schema=False)
async def yandex_verification():
    return """
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    </head>
    <body>Verification: 5ce173d08f9c739d</body>
</html>
"""