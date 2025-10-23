from fastapi import FastAPI, Query
from typing import Annotated
from core import db, config
from api.main import api_router

app = FastAPI(
    title=config.settings.project_name
)
db.create_tables()

app.include_router(api_router, prefix=config.settings.api_v1_str)

@app.get("/")
def greet(name:Annotated[str | None, Query()] = None):
    if name is not None:
        return {"message": f"hello!, {name}"}
    
    return {"message": "hello!, world"}
        