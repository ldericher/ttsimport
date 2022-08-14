import io
import logging
import re
import time
import zipfile
from typing import Iterator, Optional

import fftcgtool
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import StreamingResponse
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


class DeckBody(BaseModel):
    language: Optional[str]
    deck_id: str

    @property
    def sanitized_id(self) -> Optional[str]:
        san_id = next(fftcgtool.FFDecks.sanitized_ids([self.deck_id]))

        if san_id is not None:
            return san_id


class SummaryResponse(BaseModel):
    deck_id: str
    name: str
    card_count: int


@router.post("/summary", response_model=Optional[SummaryResponse])
async def get_deck_metadata(deck_body: DeckBody):
    if (deck_data := fftcgtool.FFDecks.get_deck_data(deck_body.sanitized_id)) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No valid deck id received."
        )

    return {
        "deck_id": deck_data["description"],
        "name": deck_data["name"],
        "card_count": sum(card["count"] for card in deck_data["cards"]),
    }


@router.post("/deck")
async def get_deck(deck_body: DeckBody):
    # sanitize language parameter
    language = RE_NO_ALPHA.sub("", deck_body.language)
    language = fftcgtool.Language(language)

    # create decks
    if not (decks := fftcgtool.FFDecks([deck_body.deck_id])):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No valid decks received."
        )

    return StreamingResponse(
        pack(decks, language),
        status_code=status.HTTP_200_OK,
        media_type="application/zip",
        headers={"Content-Disposition": "attachment; filename=decks.zip"},
    )
