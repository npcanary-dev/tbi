import argparse

import uvicorn

from tbi.api import app
from tbi.core.logging import logger

logger = logger.getChild("core.server")


def run(args: argparse.Namespace):
    logger.info("Starting TBI server.")
    try:
        uvicorn.run(app=app, host=args.address, port=args.port)
    finally:
        logger.info("TBI server stopped.")
