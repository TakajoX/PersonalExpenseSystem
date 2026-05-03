💰 Personal Expense System

Un sistema intuitivo a riga di comando (CLI) progettato per la gestione delle spese personali, la definizione di budget mensili e la generazione di report dettagliati.

🛠️ Stack Tecnologico

Il progetto è costruito utilizzando strumenti moderni per garantire un ambiente di sviluppo isolato e riproducibile:

Linguaggio: Python 3.8+

Database: PostgreSQL

Containerizzazione: Docker & Docker Compose

Ambiente di Sviluppo: Devcontainers (VS Code)

Automazione: GNU Make

📋 Requisiti di Sistema

Per eseguire il progetto, assicurati di avere installato:

Docker & Docker Compose: Per la gestione del database.

Supporto Devcontainer: Un IDE compatibile (consigliato: Visual Studio Code con estensione "Dev Containers").

[!NOTE]
All'interno del Devcontainer, strumenti come Make e l'interprete Python sono già preconfigurati e pronti all'uso.

📦 Librerie e Dipendenze

Il sistema si appoggia alle seguenti risorse:

Standard Library: os, datetime.

Librerie Esterne:

psycopg2-binary: Interazione con PostgreSQL.

python-dotenv: Gestione delle variabili d'ambiente.

⚠️ Configurazione Iniziale (.env)

Prima di avviare il sistema, è obbligatorio creare un file di configurazione:

Crea un file chiamato .env nella cartella root del progetto.

Inserisci le credenziali e le variabili d'ambiente fornite nel file PDF della documentazione.

Senza questo file, il sistema non potrà connettersi al database.

🚀 Istruzioni per l'Esecuzione

Segui questi passaggi nell'ordine indicato per configurare e avviare l'applicazione:

1. Avvio dell'Ambiente

Apri la cartella del progetto con il tuo IDE e avvia il Devcontainer. Questo isolerà l'ambiente e caricherà tutte le dipendenze necessarie.

2. Accensione del Database

Apri il terminale all'interno del container ed esegui il comando per avviare PostgreSQL in background:

docker-compose up -d


3. Inizializzazione (Migrazione)

Per creare le tabelle e caricare i dati iniziali nel database, utilizza il comando Make dedicato:

make init-db


4. Avvio dell'Applicazione

Una volta che il database è pronto, lancia il programma principale con:

make run


Questo comando avvierà l'interfaccia CLI e ti permetterà di navigare nel menu principale.

Sviluppato per la gestione intelligente delle tue finanze.