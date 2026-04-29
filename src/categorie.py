def modulo_gestione_categorie(conn):
    print("\n--- GESTIONE CATEGORIE ---[cite: 1]")
    nome = input("Inserisci il nome della nuova categoria: ").strip()

    if not nome:
        print("Errore: Il nome della categoria non può essere vuoto.[cite: 1]")
        return

    with conn.cursor() as cursor:
        cursor.execute("SELECT id FROM categorie WHERE nome = %s", (nome,))
        if cursor.fetchone():
            print("Errore: La categoria esiste già.[cite: 1]")
            return

        try:
            cursor.execute("INSERT INTO categorie (nome) VALUES (%s)", (nome,))
            conn.commit()
            print("Categoria inserita correttamente.[cite: 1]")
        except Exception as e:
            conn.rollback()
            print(f"Errore durante l'inserimento: {e}[cite: 1]")
