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
                print(
                    "\nData        Categoria         Importo   Descrizione")
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
