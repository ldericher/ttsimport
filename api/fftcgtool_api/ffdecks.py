import io
import re
import time
import zipfile

import fftcgtool
from flask import abort, Blueprint, current_app, send_file

bp = Blueprint("ffdecks", __name__, url_prefix="/ffdecks")

re_no_alpha = re.compile(r"[^a-z]+", flags=re.UNICODE | re.IGNORECASE)
re_no_num_comma = re.compile(r"[^0-9,]+", flags=re.UNICODE | re.IGNORECASE)


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


@bp.route("/<language>/<deck_ids>")
def ffdecks(language: str, deck_ids: str):
    # sanitize parameters
    language = re_no_alpha.sub("", language)
    language = fftcgtool.Language(language)
    deck_ids = re_no_num_comma.sub("", deck_ids)
    deck_ids = deck_ids.split(",")

    # log sane parameters
    current_app.logger.debug(f"{language = }, {deck_ids = }, path = {current_app.root_path}")

    # create decks
    decks = fftcgtool.TTSDeck.from_ffdecks_decks(deck_ids)
    if not decks:
        abort(400)

    return send_file(
        pack(decks, language), download_name='decks.zip', as_attachment=True
    )
