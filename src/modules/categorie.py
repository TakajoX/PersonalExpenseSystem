def modulo_gestione_categorie(conn):
    while True:
        print("\n--- GESTIONE CATEGORIE ---")
        print("1. Visualizza categorie")
        print("2. Inserisci nuova categoria")
        print("3. Elimina categoria")
        print("4. Torna al menu principale")

        scelta = input("Scegli un'opzione: ").strip()

        if scelta == '1':
            # VISUALIZZAZIONE
            with conn.cursor() as cursor:
                cursor.execute("SELECT nome FROM categorie ORDER BY nome")
                categorie = cursor.fetchall()
                if not categorie:
                    print("\nNessuna categoria presente nel database.")
                else:
                    print("\nN. | Nome Categoria")
                    print("-" * 30)
                    for i, row in enumerate(categorie, start=1):
                        print(f"{i:<2} | {row[0]}")

        elif scelta == '2':
            # INSERIMENTO
            nome = input("\nInserisci il nome della nuova categoria: ").strip()
            if not nome:
                print("Errore: Il nome della categoria non può essere vuoto.")
                continue

            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id FROM categorie WHERE LOWER(nome) = LOWER(%s)", (nome,))
                if cursor.fetchone():
                    print(
                        "Errore: La categoria esiste già.")
                    continue
                try:
                    cursor.execute(
                        "INSERT INTO categorie (nome) VALUES (%s)", (nome,))
                    conn.commit()
                    print("Categoria inserita correttamente.")
                except Exception as e:
                    conn.rollback()
                    print(f"Errore durante l'inserimento: {e}")

        elif scelta == '3':
            # ELIMINAZIONE
            nome = input(
                "\nInserisci il nome della categoria da eliminare: ").strip()
            if not nome:
                print("Errore: Il nome della categoria non può essere vuoto.")
                continue

            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nome FROM categorie WHERE LOWER(nome) = LOWER(%s)", (nome,))
                risultato = cursor.fetchone()

                if not risultato:
                    print(f"Errore: La categoria '{nome}' non esiste.")
                    continue

                categoria_id = risultato[0]
                nome_reale = risultato[1]

                # 2. Tentiamo l'eliminazione
                try:
                    cursor.execute(
                        "DELETE FROM categorie WHERE id = %s", (categoria_id,))
                    conn.commit()
                    print(f"Categoria '{nome_reale}' eliminata con successo.")
                except Exception as e:
                    conn.rollback()
                    print(
                        f"Errore durante l'eliminazione. La categoria potrebbe essere in uso nelle tue spese o budget.")
                    print(f"Dettaglio tecnico: {e}")

        elif scelta == '4':
            # USCITA DAL SOTTOMENU
            break

        else:
            print("Scelta non valida. Riprovare.")
