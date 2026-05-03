DROP TABLE IF EXISTS budget;
DROP TABLE IF EXISTS spese;
DROP TABLE IF EXISTS categorie;

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
('Intrattenimento'),
('Salute'),
('Casa'),
('Abbigliamento'),
('Istruzione'),
('Ristoranti'),
('Utenze'),
('Viaggi')
ON CONFLICT DO NOTHING;

INSERT INTO spese (data, importo, descrizione, categoria_id) VALUES 
('2025-01-15', 25.00, 'Pranzo di lavoro', 1),
('2025-01-16', 50.00, 'Abbonamento treno', 2),
('2025-01-18', 120.50, 'Spesa settimanale supermercato', 1),
('2025-01-20', 30.00, 'Biglietti cinema', 3),
('2025-01-22', 45.00, 'Farmaci da banco', 4),
('2025-01-25', 850.00, 'Affitto mensile', 5),
('2025-01-27', 65.90, 'Scarpe da ginnastica', 6),
('2025-02-02', 150.00, 'Rata corso di inglese', 7),
('2025-02-05', 85.00, 'Cena in pizzeria con amici', 8),
('2025-02-10', 115.00, 'Bolletta energia elettrica', 9);

INSERT INTO budget (mese, importo, categoria_id) VALUES 
('2025-01', 300.00, 1),
('2025-01', 100.00, 2),
('2025-01', 50.00, 3),
('2025-01', 100.00, 4),
('2025-01', 900.00, 5),
('2025-02', 350.00, 1),
('2025-02', 100.00, 2),
('2025-02', 150.00, 7),
('2025-02', 120.00, 8),
('2025-02', 150.00, 9);