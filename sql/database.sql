CREATE TABLE IF NOT EXISTS categorie (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS spese (
    id SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    importo DECIMAL(10, 2) NOT NULL CHECK (importo > 0),
    descrizione VARCHAR(255),
    categoria_id INT NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES categorie(id)
);

CREATE TABLE IF NOT EXISTS budget (
    id SERIAL PRIMARY KEY,
    mese VARCHAR(7) NOT NULL,
    importo DECIMAL(10, 2) NOT NULL CHECK (importo > 0),
    categoria_id INT NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES categorie(id),
    UNIQUE (categoria_id, mese)
);

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