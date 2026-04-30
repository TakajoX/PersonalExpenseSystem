import os
from db.database import get_db_connection


def init_database():
    print("Inizializzazione del database in corso...[cite: 1]")
    conn = get_db_connection()

    if not conn:
        print("  Impossibile connettersi al DB.[cite: 1]")
        return

    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        sql_file_path = os.path.join(base_dir, 'sql', 'database.sql')

        with open(sql_file_path, 'r') as file:
            sql_script = file.read()

        with conn.cursor() as cursor:
            cursor.execute(sql_script)
            conn.commit()
            print(
                "  Tabelle e dati di base inizializzati con successo![cite: 1]")

    except Exception as e:
        print(f"  Errore durante l'inizializzazione: {e}[cite: 1]")
    finally:
        conn.close()


if __name__ == "__main__":
    init_database()
