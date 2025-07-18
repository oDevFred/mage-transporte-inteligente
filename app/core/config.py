import os

DB_URL = os.getenv("DB_URL", "postgresql://usuario:senha@localhost:5432/mage_db")
