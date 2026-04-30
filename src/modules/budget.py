from db.database import ottieni_id_categoria


def modulo_definisci_budget(conn):
    print("\n--- DEFINISCI BUDGET MENSILE ---[cite: 1]")
    mese = input("Mese (formato YYYY-MM): ").strip()

    if len(mese) != 7 or mese[4] != '-':
        print("Errore: Formato mese non valido. Usa YYYY-MM.[cite: 1]")
        return

    nome_categoria = input("Nome della categoria: ").strip()
    categoria_id = ottieni_id_categoria(conn, nome_categoria)

    if not categoria_id:
        print("Errore: la categoria non esiste.[cite: 1]")
        return

    try:
        importo = float(input("Importo del budget: "))
        if importo <= 0:
            print("Errore: il budget deve essere maggiore di zero.[cite: 1]")
            return
    except ValueError:
        print("Errore: Inserisci un numero valido per il budget.[cite: 1]")
        return

    with conn.cursor() as cursor:
        try:
            # ON CONFLICT necessita del vincolo UNIQUE(categoria_id, mese)[cite: 1]
            cursor.execute("""
                INSERT INTO budget (mese, importo, categoria_id) 
                VALUES (%s, %s, %s)
                ON CONFLICT (categoria_id, mese) 
                DO UPDATE SET importo = EXCLUDED.importo
            """, (mese, importo, categoria_id))
            conn.commit()
            print("Budget mensile salvato correttamente.[cite: 1]")
        except Exception as e:
            conn.rollback()
            print(f"Errore durante l'inserimento: {e}[cite: 1]")
