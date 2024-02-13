compose-build:
	docker network create data-eng-network --driver=bridge
	docker compose -f ./airflow/docker-compose.yaml build
	docker compose -f ./spark/docker-compose.yaml build
	docker compose -f ./jupyter/docker-compose.yaml build


.PHONY: compose-build