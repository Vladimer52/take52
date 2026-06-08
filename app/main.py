from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.core.paths import STATIC_DIR
from app.routes import pages, system


def create_app() -> FastAPI:
    app = FastAPI(title="TAKE52")

    app.mount(
        "/static",
        StaticFiles(directory=STATIC_DIR),
        name="static",
    )

    app.include_router(pages.router)
    app.include_router(system.router)

    return app


app = create_app()