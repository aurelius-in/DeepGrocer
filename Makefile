.PHONY: up down logs db seed agents ui api fmt

up:
	docker compose -f infra/docker/docker-compose.yml up -d --build

down:
	docker compose -f infra/docker/docker-compose.yml down -v

logs:
	docker compose -f infra/docker/docker-compose.yml logs -f --tail=200

db:
	psql postgresql://dg:dgpass@localhost:5432/deepgrocer -f infra/sql/001_init.sql && \
	psql postgresql://dg:dgpass@localhost:5432/deepgrocer -f infra/sql/002_receipts.sql

seed:
	python scripts/seed_synthetic_day.py

agents:
	docker compose -f infra/docker/docker-compose.yml restart worker

api:
	docker compose -f infra/docker/docker-compose.yml restart api

ui:
	docker compose -f infra/docker/docker-compose.yml restart ui

