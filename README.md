Personal Expense System

Un sistema a riga di comando per la gestione delle spese personali, la definizione di budget mensili e la visualizzazione di report dettagliati.

Requisiti per l'esecuzione

Per eseguire correttamente questo progetto, è necessario avere installato il seguente software sulla propria macchina locale:

Docker e Docker Compose: Necessari per avviare il container del database PostgreSQL.

Supporto Devcontainer: Un IDE compatibile con gli ambienti basati su container (es. utilizzando l'estensione "Dev Containers" su Visual Studio Code).

Nota bene: I seguenti strumenti sono già disponibili e preconfigurati all'interno del Devcontainer, pertanto non è necessario installarli manualmente sul proprio computer:

Make: Strumento necessario per lanciare i comandi automatizzati presenti nel Makefile.

Interprete Python: Versione 3.8 o superiore (ambiente e dipendenze pronti all'uso).

Librerie e Dipendenze

Il progetto utilizza le seguenti librerie:

Librerie Standard Python: os, datetime.

Librerie Esterne:

psycopg2-binary: Per la connessione e l'interazione con il database PostgreSQL.

python-dotenv: Per il caricamento delle variabili d'ambiente dal file di configurazione.

Configurazione Iniziale

ATTENZIONE: Chiunque cloni o scarichi questo progetto deve creare manualmente un file .env nella cartella principale (root) del progetto.
Le informazioni specifiche, le credenziali e le variabili d'ambiente da inserire all'interno di questo file si trovano all'interno del file PDF fornito insieme alla documentazione del progetto.

Senza il file .env correttamente configurato, il sistema non sarà in grado di comunicare con il database.

Istruzioni dettagliate per eseguire il programma

Segui questi passaggi nell'ordine esatto per configurare e avviare il programma:

1. Avvio dell'ambiente Devcontainer

Apri il progetto in un IDE supportato (come Visual Studio Code) e avvia il Devcontainer. Questo garantirà che l'ambiente Python e tutti gli strumenti di compilazione siano isolati e pronti all'uso.

2. Avvio del Database (Docker Compose)

Una volta all'interno dell'ambiente, è necessario avviare il container del database PostgreSQL. Esegui il seguente comando nel terminale:

docker-compose up -d


Questo comando scaricherà l'immagine di PostgreSQL e avvierà il database in background.

3. Migrazione e Inizializzazione del Database

Prima di poter utilizzare l'applicazione, bisogna creare le tabelle e inserire i dati di base. Puoi farlo automaticamente grazie al Makefile incluso.
Esegui questo comando esatto:

make init-db


Questo comando eseguirà lo script SQL all'interno del container Docker appena creato, predisponendo il database per l'utilizzo.

4. Avvio del Programma

Una volta che il database è configurato e in esecuzione, puoi avviare l'interfaccia a riga di comando del programma eseguendo:

make run


Questo comando invocherà l'interprete Python sul file src/main.py, permettendoti di accedere al menu principale del sistema.