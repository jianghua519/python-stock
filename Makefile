# Makefile

.PHONY: up down build logs test format

up:
	docker-compose up -d

down:
	docker-compose down

build:
	docker-compose build

logs:
	docker-compose logs -f

test:
	pytest tests/

format:
	black services/ shared/ tests/
