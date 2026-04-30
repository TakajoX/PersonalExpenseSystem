from db.database import get_db_connection
from modules.categorie import modulo_gestione_categorie
from modules.spese import modulo_inserisci_spesa
from modules.budget import modulo_definisci_budget
from modules.report import modulo_visualizza_report


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
        print("1. Gestione Categorie[cite: 1]")
        print("2. Inserisci Spesa[cite: 1]")
        print("3. Definisci Budget Mensile[cite: 1]")
        print("4. Visualizza Report[cite: 1]")
        print("5. Esci[cite: 1]")
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
