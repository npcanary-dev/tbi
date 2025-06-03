from fastapi import FastAPI

from tbi.api import main

app = FastAPI(title="TBI")

app.include_router(main.router)
