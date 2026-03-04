from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

def execute_query(sql: str):
    """
    Execute a SQL statement.
    Returns (rows, columns) or raises RuntimeError.
    """
    try:
        with engine.connect() as conn:
            result = conn.execute(text(sql))

            columns = list(result.keys())
            rows = [dict(zip(columns, row)) for row in result.fetchall()]

            return rows, columns

    except SQLAlchemyError as exc:
        raise RuntimeError(str(exc)) from exc