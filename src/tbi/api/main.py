from typing import Any, Dict

from fastapi import APIRouter

from tbi.core.logging import logger
from tbi.tibia.characters import fetch_character

logger = logger.getChild("api.main")

router = APIRouter()


@router.get("/{charname}")
async def get_character_data(charname: str) -> Dict[str, Any]:
    logger.info("Character fetching request received.")
    return await fetch_character(charname)
