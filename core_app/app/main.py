from fastapi import FastAPI, Query
from typing import Annotated
from core import db, config
from api.main import api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title=config.settings.project_name)
origins = "http://localhost:*"


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_origin_regex=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db.create_tables()

app.include_router(api_router, prefix=config.settings.api_v1_str)
