import logging
import os
from logging.config import dictConfig

import fftcgtool
import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .config import settings, log_config
from .ffdecks import router as ffdecks_router

dictConfig(log_config.dict())

# create app
app = FastAPI(
    title="TTSImport API",
    description="This API provides `fftcgtool` over HTTP.",
    version="0.4.0",
    contact={
        "name": "LDericher",
        "email": "LDericher@GMX.de",
    },
    license_info={
        "name": "GPLv3",
        "url": "https://www.gnu.org/licenses/gpl-3.0.en.html",
    },
    openapi_url=settings.openapi_url,
    docs_url=settings.docs_url if not settings.production_mode else None,
    redoc_url=settings.redoc_url if not settings.production_mode else None,
)
app.include_router(
    router=ffdecks_router,
    prefix="/api",
)


@app.on_event("startup")
def main():
    if settings.production_mode:
        # Mount frontend in production mode
        app.mount(
            path="/",
            app=StaticFiles(
                directory="/html",
                html=True,
            ),
            name="frontend",
        )

    else:
        # Allow CORS in debug mode
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[
                "*",
            ],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    logger = logging.getLogger(__name__)
    logger.info(f"{settings = }")

    # card db
    here = os.path.dirname(os.path.realpath(__file__))
    fftcgtool.CardDB(os.path.join(here, "carddb.zip"))

    return app


@app.middleware("http")
async def add_cache_control_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["Cache-Control"] = "max-age=86400"
    return response


if __name__ == "__main__":
    uvicorn.run(
        "ttsimport.main:app",
        host="0.0.0.0",
        port=5000,
        reload=True,
    )
