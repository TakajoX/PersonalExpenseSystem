from db.database import ottieni_id_categoria


def modulo_definisci_budget(conn):
    print("\n--- DEFINISCI BUDGET MENSILE ---")
    mese = input("Mese (formato YYYY-MM): ").strip()
    if len(mese) != 7 or mese[4] != '-':
        print("Errore: Formato mese non valido. Usa YYYY-MM.")
        return

    with conn.cursor() as cursor:
        cursor.execute("SELECT nome FROM categorie ORDER BY nome")
        categorie = cursor.fetchall()

        if not categorie:
            print("\nAttenzione: Nessuna categoria presente nel database. Vai prima in 'Gestione Categorie' per crearne una.")
            return

        nomi_categorie = [row[0] for row in categorie]
        print(f"\nCategorie disponibili: {', '.join(nomi_categorie)}")

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
