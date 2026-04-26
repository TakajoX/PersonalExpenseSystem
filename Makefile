

init-db:
	@echo "Inizializzazione del database in corso..."
	docker exec -i personal_expense_db psql -U admin -d spese_db < sql/database.sql
	@echo "Completato!"

run:
	python src/main.py