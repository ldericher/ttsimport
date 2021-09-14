import io
import logging
import re
import time
import zipfile
from typing import Iterator, Optional

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


class DecksBody(BaseModel):
    language: Optional[str]
    deck_ids: list[str]

    @property
    def sanitized_ids(self) -> Iterator[str]:
        return (
            deck_id
            for deck_id in fftcgtool.FFDecks.sanitized_ids(self.deck_ids)
            if deck_id is not None
        )


class CheckResponse(BaseModel):
    deck_id: str
    exists: bool


@router.post("/check", response_model=list[CheckResponse])
async def check_decks(decks_body: DecksBody):
    return ({
        "deck_id": deck_id,
        "exists": fftcgtool.FFDecks.get_deck_data(deck_id) is not None
    } for deck_id in decks_body.sanitized_ids)


class SummaryResponse(BaseModel):
    deck_id: str
    name: str
    card_count: int


@router.post("/summaries", response_model=list[SummaryResponse])
async def get_deck_names(decks_body: DecksBody):
    return (
        {
            "deck_id": deck_data["description"],
            "name": deck_data["name"],
            "card_count": sum(card["count"] for card in deck_data["cards"]),
        } for deck_id in decks_body.sanitized_ids
        if (deck_data := fftcgtool.FFDecks.get_deck_data(deck_id)) is not None
    )


@router.post("/deck")
async def get_decks(decks_body: DecksBody):
    # sanitize language parameter
    language = RE_NO_ALPHA.sub("", decks_body.language)
    language = fftcgtool.Language(language)

    # create decks
    if not (decks := fftcgtool.FFDecks(decks_body.sanitized_ids)):
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
