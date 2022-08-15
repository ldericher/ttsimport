import logging
import re
from typing import Optional

from fastapi import APIRouter, HTTPException, Response, status
from fftcgtool import FFDecks, Language
from pydantic import BaseModel

RE_NO_ALPHA = re.compile(r"[^a-z]+", flags=re.UNICODE | re.IGNORECASE)
router = APIRouter(prefix="/ffdecks")


class DeckBody(BaseModel):
    language: Optional[str]
    deck_id: str

    @property
    def sanitized_id(self) -> Optional[str]:
        san_id = next(FFDecks.sanitized_ids([self.deck_id]))

        if san_id is not None:
            return san_id


class SummaryResponse(BaseModel):
    deck_id: str
    name: str
    card_count: int


@router.post("/summary", response_model=Optional[SummaryResponse])
async def get_deck_metadata(deck_body: DeckBody):
    if (deck_data := FFDecks.get_deck_data(deck_body.sanitized_id)) is None:
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
    logger = logging.getLogger(__name__)

    # sanitize language parameter
    language = RE_NO_ALPHA.sub("", deck_body.language)
    language = Language(language)

    # create decks
    if not (decks := FFDecks([deck_body.deck_id])):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No valid decks received."
        )

    deck = decks[0]
    logger.info(f"Saving Deck {deck!r}")

    return Response(
        deck.get_json(language),
        status_code=status.HTTP_200_OK,
        media_type="application/json, text/plain",
        headers={
            "Content-Disposition": f"attachment; filename={deck.file_name}"
        },
    )
