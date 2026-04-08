import sqlite3
from pathlib import Path

DB_FILEPATH = Path('./dev.db')

DB_CONN = sqlite3.connect(DB_FILEPATH)