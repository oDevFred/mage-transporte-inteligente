from decouple import config

DB_URL = config("DB_URL")
print(f"Conectando ao banco: {DB_URL}")
