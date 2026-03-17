from sqlalchemy import create_engine, text
from config import settings


engine = create_engine(settings.database_url, future=True)


def init_db() -> None:
    with engine.begin() as conn:
        conn.execute(text("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, title TEXT NOT NULL)"))
        conn.execute(text("INSERT INTO notes (title) VALUES ('Hello from Flask boilerplate')"))


def read_notes() -> list[dict]:
    with engine.connect() as conn:
        rows = conn.execute(text("SELECT id, title FROM notes ORDER BY id DESC LIMIT 5"))
        return [{"id": row.id, "title": row.title} for row in rows]
