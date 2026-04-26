-- Creazione tabella Categorie
CREATE TABLE IF NOT EXISTS categorie (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) UNIQUE NOT NULL
);

-- Creazione tabella Spese
CREATE TABLE IF NOT EXISTS spese (
    id SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    importo DECIMAL(10, 2) NOT NULL CHECK (importo > 0),
    descrizione VARCHAR(255),
    categoria_id INT NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES categorie(id)
);

-- Inserimento dati di esempio
INSERT INTO categorie (nome) VALUES ('Alimentari'), ('Trasporti') ON CONFLICT DO NOTHING;