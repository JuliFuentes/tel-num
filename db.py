import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Crear la conexión
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()
