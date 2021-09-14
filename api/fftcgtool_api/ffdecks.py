import io
import re
import time
import zipfile

import fftcgtool
from flask import abort, Blueprint, current_app, send_file, request

bp = Blueprint("ffdecks", __name__, url_prefix="/ffdecks")

RE_NO_ALPHA = re.compile(r"[^a-z]+", flags=re.UNICODE | re.IGNORECASE)


def pack(decks: list[fftcgtool.TTSDeck], language: fftcgtool.Language) -> io.BytesIO:
    # create an in-memory file
    mem_file = io.BytesIO()

    # zip the decks into mem_file
    with zipfile.ZipFile(mem_file, "w", compression=zipfile.ZIP_DEFLATED) as zip_file:
        for deck in decks:
            # time info
            data = zipfile.ZipInfo(deck.file_name)
            data.date_time = time.localtime(time.time())[:6]

            current_app.logger.debug(f"Saving Deck {deck!r}")
            zip_file.writestr(deck.file_name, deck.get_json(language))

    # rewind in-memory file before returning
    mem_file.seek(0)
    return mem_file


@bp.route("/<language>", methods=["POST"])
def ffdecks(language: str):
    # sanitize parameters
    language = RE_NO_ALPHA.sub("", language)
    language = fftcgtool.Language(language)

    content = request.get_json()
    deck_ids = [
        deck_id
        for deck_id in fftcgtool.FFDecks.sanitized_ids(content["deck_ids"])
        if deck_id is not None
    ]

    # log sane parameters
    current_app.logger.debug(f"{language = }, {deck_ids = }")

    # create decks
    decks = fftcgtool.FFDecks(deck_ids)
    if not decks:
        abort(400)

    return send_file(
        pack(decks, language), download_name='decks.zip', as_attachment=True
    )
