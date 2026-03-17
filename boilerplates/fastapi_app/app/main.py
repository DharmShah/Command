from fastapi import FastAPI
from .db import init_db, list_items


app = FastAPI(title="FastAPI Boilerplate")


@app.on_event("startup")
def startup() -> None:
    init_db()


@app.get("/")
def read_root() -> dict:
    return {"message": "FastAPI boilerplate running", "items": list_items()}
