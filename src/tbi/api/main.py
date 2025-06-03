from typing import Any, Dict

from fastapi import APIRouter

from tbi.core.logging import logger
from tbi.tibia.characters import fetch_character
from tbi.database import schemas

logger = logger.getChild("api.main")

router = APIRouter()


@router.get("/api/{charname}", response_model=schemas.CharacterData)
async def get_character_data(charname: str) -> Dict[str, Any]:
    logger.info("Character fetching request received.")
    return await fetch_character(charname)
