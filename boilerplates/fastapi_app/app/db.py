from sqlalchemy import create_engine, text
from .config import settings


engine = create_engine(settings.database_url, future=True)


def init_db() -> None:
    with engine.begin() as conn:
        conn.execute(text("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT NOT NULL)"))
        conn.execute(text("INSERT INTO items (name) VALUES ('FastAPI demo item')"))


def list_items() -> list[dict]:
    with engine.connect() as conn:
        rows = conn.execute(text("SELECT id, name FROM items ORDER BY id DESC LIMIT 5"))
        return [{"id": row.id, "name": row.name} for row in rows]
