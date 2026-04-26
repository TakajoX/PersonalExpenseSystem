import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_db_connection():
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


def init_database():
    """Legge il file database.sql e inizializza le tabelle."""
    conn = get_db_connection()
    if not conn:
        return False

    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        sql_file_path = os.path.join(base_dir, 'sql', 'database.sql')

        with open(sql_file_path, 'r') as file:
            sql_script = file.read()

        with conn.cursor() as cursor:
            cursor.execute(sql_script)
            conn.commit()
            print("Tabelle e dati di base inizializzati con successo!")
        return True
    except Exception as e:
        print(f"Errore durante l'inizializzazione del database: {e}")
        return False
    finally:
        conn.close()


def main_menu():
    print("Avvio del sistema in corso...")

    if not init_database():
        print("Impossibile avviare il sistema. Controllare il database.")
        return

    while True:
        print("\n-------------------------")
        print(" SISTEMA SPESE PERSONALI")
        print("-------------------------")
        print("1. Gestione Categorie")
        print("2. Inserisci Spesa")
        print("3. Definisci Budget Mensile")
        print("4. Visualizza Report")
        print("5. Esci")
        print("-------------------------")

        scelta = input("Inserisci la tua scelta: ")

        if scelta == '1':
            print("Modulo Categorie non ancora implementato.")
        elif scelta == '5':
            print("Uscita dal programma. Arrivederci!")
            break
        else:
            print("Scelta non valida. Riprovare.")


if __name__ == "__main__":
    main_menu()
