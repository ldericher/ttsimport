import os

import fftcgtool
import uvicorn
from fastapi import FastAPI
from fastapi.logger import logger
from fastapi.middleware.cors import CORSMiddleware

from ttsimport.config import settings
from .ffdecks import router as ffdecks_router


def main() -> FastAPI:
    logger.warning(settings)

    # create app
    app = FastAPI(
        title="TTSImport API",
        description="",
        version="0.1",
        license_info={
            "name": "GPLv3",
            "url": "https://www.gnu.org/licenses/gpl-3.0.en.html",
        },
        openapi_url=settings.openapi_url,
        docs_url=settings.docs_url if not settings.production_mode else None,
        redoc_url=settings.redoc_url if not settings.production_mode else None,
    )
    app.include_router(ffdecks_router)

    # Allow CORS in debug mode
    # production mode will have a reverse proxy
    if not settings.production_mode:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[
                "http://localhost",
                "https://localhost",
            ],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    # card db
    dbpath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "carddb.zip")
    fftcgtool.CardDB(dbpath)

    return app


if __name__ == "__main__":
    uvicorn.run(
        "ttsimport.main:main",
        host="0.0.0.0",
        port=8000,
        reload=True,
        factory=True,
    )
