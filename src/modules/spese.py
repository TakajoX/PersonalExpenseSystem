from datetime import datetime
from db.database import ottieni_id_categoria


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

    # Validazione categori
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
