from pathlib import Path

from sqlalchemy import Engine, create_engine

DB_PATH = Path(r"D:\Projects\Database\Sqlite\pyref.db")
ENGINE: Engine = create_engine(f"sqlite:///{DB_PATH}")
