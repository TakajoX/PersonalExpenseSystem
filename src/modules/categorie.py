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
