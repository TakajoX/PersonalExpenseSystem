import os
import psycopg2
from dotenv import load_dotenv
from datetime import datetime

# Carica le variabili d'ambiente
load_dotenv()


def get_db_connection():
    """Tenta di stabilire una connessione con il database[cite: 1]."""
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

# --- FUNZIONI DI SUPPORTO ---


def ottieni_id_categoria(conn, nome_categoria):
    """Restituisce l'ID della categoria dal nome, o None se non esiste."""
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT id FROM categorie WHERE nome = %s", (nome_categoria,))
        risultato = cursor.fetchone()
        return risultato[0] if risultato else None

# --- MODULI DEL PROGETTO ---


def modulo_gestione_categorie(conn):
    print("\n--- GESTIONE CATEGORIE ---")
    nome = input("Inserisci il nome della nuova categoria: ").strip()

    if not nome:
        print("Errore: Il nome della categoria non può essere vuoto.")
        return

    with conn.cursor() as cursor:
        cursor.execute("SELECT id FROM categorie WHERE nome = %s", (nome,))
        if cursor.fetchone():
            print("Errore: La categoria esiste già.")
            return

        try:
            cursor.execute("INSERT INTO categorie (nome) VALUES (%s)", (nome,))
            conn.commit()
            print("Categoria inserita correttamente.")
        except Exception as e:
            conn.rollback()
            print(f"Errore durante l'inserimento: {e}")


def modulo_inserisci_spesa(conn):
    print("\n--- INSERISCI SPESA ---")
    data_str = input("Data (formato YYYY-MM-DD): ").strip()

    # Validazione data
    try:
        datetime.strptime(data_str, "%Y-%m-%d")
    except ValueError:
        print("Errore: Formato data non valido. Usa YYYY-MM-DD.")
        return

    # Validazione importo
    try:
        importo = float(input("Importo: "))
        if importo <= 0:
            print("Errore: l'importo deve essere maggiore di zero.")
            return
    except ValueError:
        print("Errore: Inserisci un numero valido per l'importo.")
        return

    # Validazione categoria
    nome_categoria = input("Nome della categoria: ").strip()
    categoria_id = ottieni_id_categoria(conn, nome_categoria)
    if not categoria_id:
        print("Errore: la categoria non esiste.")
        return

    descrizione = input("Descrizione (facoltativa): ").strip()

    with conn.cursor() as cursor:
        try:
            cursor.execute(
                "INSERT INTO spese (data, importo, categoria_id, descrizione) VALUES (%s, %s, %s, %s)",
                (data_str, importo, categoria_id, descrizione)
            )
            conn.commit()
            print("Spesa inserita correttamente.")
        except Exception as e:
            conn.rollback()
            print(f"Errore durante l'inserimento: {e}")


def modulo_definisci_budget(conn):
    print("\n--- DEFINISCI BUDGET MENSILE ---")
    mese = input("Mese (formato YYYY-MM): ").strip()

    if len(mese) != 7 or mese[4] != '-':
        print("Errore: Formato mese non valido. Usa YYYY-MM.")
        return

    nome_categoria = input("Nome della categoria: ").strip()
    categoria_id = ottieni_id_categoria(conn, nome_categoria)
    if not categoria_id:
        print("Errore: la categoria non esiste.")
        return

    try:
        importo = float(input("Importo del budget: "))
        if importo <= 0:
            print("Errore: il budget deve essere maggiore di zero.")
            return
    except ValueError:
        print("Errore: Inserisci un numero valido per il budget.")
        return

    with conn.cursor() as cursor:
        try:
            # ON CONFLICT necessita del vincolo UNIQUE(categoria_id, mese)
            cursor.execute("""
                INSERT INTO budget (mese, importo, categoria_id) 
                VALUES (%s, %s, %s)
                ON CONFLICT (categoria_id, mese) 
                DO UPDATE SET importo = EXCLUDED.importo
            """, (mese, importo, categoria_id))
            conn.commit()
            print("Budget mensile salvato correttamente.")
        except Exception as e:
            conn.rollback()
            print(f"Errore durante l'inserimento: {e}")


def modulo_visualizza_report(conn):
    while True:
        print("\n--- MENU REPORT ---")
        print("1. Totale spese per categoria")
        print("2. Spese mensili vs budget")
        print("3. Elenco completo delle spese ordinate per data")
        print("4. Ritorna al menu principale")

        scelta = input("Scegli un report: ").strip()

        with conn.cursor() as cursor:
            if scelta == '1':
                print("\nCategoria........Totale Speso")
                cursor.execute("""
                    SELECT c.nome, SUM(s.importo) 
                    FROM spese s 
                    JOIN categorie c ON s.categoria_id = c.id 
                    GROUP BY c.nome
                """)
                for row in cursor.fetchall():
                    print(f"{row[0]:<17}{row[1]:.2f}")

            elif scelta == '2':
                print("\n--- SPESE VS BUDGET ---")
                # Query avanzata per combinare Budget e Spese
                cursor.execute("""
                    SELECT b.mese, c.nome, b.importo as budget, 
                           COALESCE(SUM(s.importo), 0) as speso
                    FROM budget b
                    JOIN categorie c ON b.categoria_id = c.id
                    LEFT JOIN spese s ON s.categoria_id = c.id 
                         AND TO_CHAR(s.data, 'YYYY-MM') = b.mese
                    GROUP BY b.mese, c.nome, b.importo
                """)
                for row in cursor.fetchall():
                    mese, cat_nome, budget, speso = row
                    stato = "SUPERAMENTO BUDGET" if speso > budget else "ENTRO IL BUDGET"
                    print(
                        f"Mese: {mese} | Categoria: {cat_nome} | Budget: {budget:.2f} | Speso: {speso:.2f} | Stato: {stato}")

            elif scelta == '3':
                print("\nData        Categoria         Importo   Descrizione")
                print("-" * 60)
                cursor.execute("""
                    SELECT s.data, c.nome, s.importo, s.descrizione 
                    FROM spese s 
                    JOIN categorie c ON s.categoria_id = c.id 
                    ORDER BY s.data
                """)
                for row in cursor.fetchall():
                    desc = row[3] if row[3] else ""
                    print(
                        f"{str(row[0]):<11} {row[1]:<17} {row[2]:<9.2f} {desc}")

            elif scelta == '4':
                break
            else:
                print("Scelta non valida.")

# --- MENU PRINCIPALE ---


def main_menu():
    print("Avvio del sistema in corso...[cite: 1]")
    conn = get_db_connection()
    if not conn:
        print(
            "Impossibile avviare il sistema. Verifica che il database (o Docker) sia attivo.[cite: 1]")
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

        scelta = input("Inserisci la tua scelta: ").strip()

        if scelta == '1':
            modulo_gestione_categorie(conn)
        elif scelta == '2':
            modulo_inserisci_spesa(conn)
        elif scelta == '3':
            modulo_definisci_budget(conn)
        elif scelta == '4':
            modulo_visualizza_report(conn)
        elif scelta == '5':
            print("Uscita dal programma. Arrivederci![cite: 1]")
            break
        else:
            print("Scelta non valida. Riprovare.[cite: 1]")

    conn.close()


if __name__ == "__main__":
    main_menu()
