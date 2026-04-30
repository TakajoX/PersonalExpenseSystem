import os
import psycopg2
from dotenv import load_dotenv

# Carica le variabili d'ambiente
load_dotenv()


def get_db_connection():
    """Tenta di stabilire una connessione con il database."""
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return conn
    except Exception as e:
        print(f"Errore di connessione al database: {e}")
        return None


def ottieni_id_categoria(conn, nome_categoria):
    """Restituisce l'ID della categoria dal nome, o None se non esiste[cite: 1]."""
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT id FROM categorie WHERE nome = %s", (nome_categoria,))
        risultato = cursor.fetchone()
        return risultato[0] if risultato else None
