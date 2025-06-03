import argparse
import asyncio
import json

from tbi.core.logging import logger
from tbi.tibia.characters import fetch_character

logger = logger.getChild("core.client")


def run(args: argparse.Namespace):
    if args.charname is not None:
        data = asyncio.run(fetch_character(args.charname))
        print(json.dumps(data, indent=4, default=str))
    else:
        logger.error(f"{args.charname=}")
