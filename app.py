from dotenv import load_dotenv
load_dotenv()
import psycopg2
import os

# Leer la variable de entorno DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Conectarse a la base de datos usando psycopg2
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

# Crear tabla si no existe
cur.execute("""
CREATE TABLE IF NOT EXISTS telefonos (
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    numero TEXT
)
""")
conn.commit()

# Insertar un contacto de ejemplo
cur.execute("INSERT INTO telefonos (nombre, numero) VALUES (%s, %s)", ("dbgenerador", "kL68iA7ThtraV92wWzRAOPRs2QuB9p9e"))
conn.commit()

# Leer y mostrar todos los contactos
cur.execute("SELECT * FROM telefonos")
registros = cur.fetchall()
print("Contactos guardados:")
for r in registros:
    print(r)

# Cerrar la conexión
cur.close()
conn.close()
