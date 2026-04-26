import os
import psycopg2
from dotenv import load_dotenv

# Carica le variabili d'ambiente dal file .env
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


def main_menu():
    # Testiamo la connessione all'avvio
    conn = get_db_connection()
    if conn:
        print("Connessione al database stabilita con successo!")
        conn.close()
    else:
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
