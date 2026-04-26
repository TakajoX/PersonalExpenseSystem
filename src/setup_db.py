import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_db_connection():
    try:
        return psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
    except Exception as e:
        print(f"Errore: {e}")
        return None


def init_database():
    print("Inizializzazione del database in corso...")
    conn = get_db_connection()
    if not conn:
        print("❌ Impossibile connettersi al DB.")
        return

    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        sql_file_path = os.path.join(base_dir, 'sql', 'database.sql')

        with open(sql_file_path, 'r') as file:
            sql_script = file.read()

        with conn.cursor() as cursor:
            cursor.execute(sql_script)
            conn.commit()
            print("✅ Tabelle e dati di base inizializzati con successo!")
    except Exception as e:
        print(f"❌ Errore durante l'inizializzazione: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    init_database()
