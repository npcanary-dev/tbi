from typing import Any, Dict

import tibiapy

from tbi.core.logging import logger

logger = logger.getChild("tibia.characters")


async def fetch_character(charname: str) -> Dict[str, Any]:
    logger.info(f"Fetching {charname!r} character data.")

    client = tibiapy.Client()
    try:
        character = await client.fetch_character(charname)
        if character is not None:
            # Return character data, skip TibiaResponse metadata
            return character.model_dump()["data"]
        else:
            raise Exception(f"Character {charname!r} not found.")
    except Exception:
        logger.exception(f"Could not fetch {charname!r} character data.")
        raise
    finally:
        await client.session.close()
