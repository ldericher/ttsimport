import io
import logging
import re
import time
import zipfile

import fftcgtool
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse, StreamingResponse
from pydantic import BaseModel

RE_NO_ALPHA = re.compile(r"[^a-z]+", flags=re.UNICODE | re.IGNORECASE)
router = APIRouter(prefix="/ffdecks")


def pack(decks: list[fftcgtool.TTSDeck], language: fftcgtool.Language) -> io.BytesIO:
    logger = logging.getLogger(__name__)

    # create an in-memory file
    mem_file = io.BytesIO()

    # zip the decks into mem_file
    with zipfile.ZipFile(mem_file, "w", compression=zipfile.ZIP_DEFLATED) as zip_file:
        for deck in decks:
            # time info
            data = zipfile.ZipInfo(deck.file_name)
            data.date_time = time.localtime(time.time())[:6]

            logger.info(f"Saving Deck {deck!r}")
            zip_file.writestr(deck.file_name, deck.get_json(language))

    # rewind in-memory file before returning
    mem_file.seek(0)
    return mem_file


class GetDecksBody(BaseModel):
    deck_ids: list[str]


@router.post("/{language}")
async def get_decks(language: str, get_decks_body: GetDecksBody):
    logger = logging.getLogger("uvicorn")

    # sanitize parameters
    language = RE_NO_ALPHA.sub("", language)
    language = fftcgtool.Language(language)

    deck_ids = [
        deck_id
        for deck_id in fftcgtool.FFDecks.sanitized_ids(get_decks_body.deck_ids)
        if deck_id is not None
    ]

    # log sane parameters
    logger.info(f"{language = }, {deck_ids = }")

    # create decks
    if not (decks := fftcgtool.FFDecks(deck_ids)):
        return JSONResponse(
            None,
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    return StreamingResponse(
        pack(decks, language),
        status_code=status.HTTP_200_OK,
        media_type="application/zip",
        headers={"Content-Disposition": "attachment; filename=decks.zip"},
    )
