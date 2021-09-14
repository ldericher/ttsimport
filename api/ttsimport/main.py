import os

import fftcgtool
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .ffdecks import router as ffdecks_router


def main() -> FastAPI:
    # create app
    app = FastAPI()
    app.include_router(ffdecks_router)

    # Allow CORS in debug mode
    # production mode will have a reverse proxy
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
