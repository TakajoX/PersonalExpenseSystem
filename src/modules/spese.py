from datetime import datetime
from db.database import ottieni_id_categoria


def modulo_inserisci_spesa(conn):
    print("\n--- INSERISCI SPESA ---[cite: 1]")
    data_str = input("Data (formato YYYY-MM-DD): ").strip()

    # Validazione data[cite: 1]
    try:
        datetime.strptime(data_str, "%Y-%m-%d")
    except ValueError:
        print("Errore: Formato data non valido. Usa YYYY-MM-DD.[cite: 1]")
        return

    # Validazione importo[cite: 1]
    try:
        importo = float(input("Importo: "))
        if importo <= 0:
            print("Errore: l'importo deve essere maggiore di zero.[cite: 1]")
            return
    except ValueError:
        print("Errore: Inserisci un numero valido per l'importo.[cite: 1]")
        return

    # Validazione categoria[cite: 1]
    nome_categoria = input("Nome della categoria: ").strip()
    categoria_id = ottieni_id_categoria(conn, nome_categoria)

    if not categoria_id:
        print("Errore: la categoria non esiste.[cite: 1]")
        return

    descrizione = input("Descrizione (facoltativa): ").strip()

    with conn.cursor() as cursor:
        try:
            cursor.execute(
                "INSERT INTO spese (data, importo, categoria_id, descrizione) VALUES (%s, %s, %s, %s)",
                (data_str, importo, categoria_id, descrizione)
            )
            conn.commit()
            print("Spesa inserita correttamente.[cite: 1]")
        except Exception as e:
            conn.rollback()
            print(f"Errore durante l'inserimento: {e}[cite: 1]")
