-- 1. Creazione tabella Categorie
CREATE TABLE IF NOT EXISTS categorie (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) UNIQUE NOT NULL
);

-- 2. Creazione tabella Spese
CREATE TABLE IF NOT EXISTS spese (
    id SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    importo DECIMAL(10, 2) NOT NULL CHECK (importo > 0),
    descrizione VARCHAR(255),
    categoria_id INT NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES categorie(id)
);

-- 3. Creazione tabella Budget (NUOVA)
CREATE TABLE IF NOT EXISTS budget (
    id SERIAL PRIMARY KEY,
    mese VARCHAR(7) NOT NULL, -- Memorizza il formato 'YYYY-MM' richiesto dall'input
    importo DECIMAL(10, 2) NOT NULL CHECK (importo > 0),
    categoria_id INT NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES categorie(id),
    UNIQUE (categoria_id, mese) -- Garantisce che ci sia un solo budget per categoria ogni mese
);

-- 4. Inserimento dati di esempio (Richiesto dal punto 8.1.b)
INSERT INTO categorie (nome) VALUES 
('Alimentari'), 
('Trasporti'), 
('Intrattenimento') 
ON CONFLICT DO NOTHING;

INSERT INTO spese (data, importo, descrizione, categoria_id) VALUES 
('2025-01-15', 25.00, 'Pranzo di lavoro', 1),
('2025-01-16', 50.00, 'Abbonamento treno', 2);

INSERT INTO budget (mese, importo, categoria_id) VALUES 
('2025-01', 300.00, 1),
('2025-01', 100.00, 2);