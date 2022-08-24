import logging
import os

from discord.ext import commands
from discord.ui import View
from fftcgtool import FFDecks

from .decklangselect import DeckLangSelect

_logger = logging.getLogger(__name__)


@commands.command()
async def decks(
    ctx: commands.Context,
    *deck_ids: str
) -> None:

    MAX_DECKS = int(os.getenv("TTSBOT_MAX_DECKS", 10))
    requester = f"{ctx.author.name}#{ctx.author.discriminator}"
    san_ids = list(FFDecks.sanitized_ids(deck_ids))

    reply_content = ""
    _logger.info(f"{requester} requested {len(san_ids)} decks.")

    if len(san_ids) > MAX_DECKS:
        san_ids = san_ids[:MAX_DECKS]
        reply_content += \
            "To keep things sane, I will only look at the first " + \
            f"{MAX_DECKS} of your deck IDs.\n"

        _logger.info(
            f"Truncated {requester}'s request to {MAX_DECKS} decks."
        )

    if (decks := FFDecks(san_ids)):
        reply_content += \
            "I found and imported the following decks for you:\n" + \
            "\n".join("• " + deck.name for deck in decks)

        _logger.info(f"Waiting for {requester} to pick deck language …")

        await ctx.reply(
            content=reply_content,
            view=View().add_item(DeckLangSelect(decks)),
        )

    else:
        reply_content += \
            "Unfortunately, I didn't find any valid decks for your " + \
            "request :cry:"

        await ctx.reply(
            content=reply_content,
        )
