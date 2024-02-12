compose-build:
	docker network create spark-airflow --driver=bridge
	docker compose -f docker-compose-airflow.yaml build
	docker compose -f docker-compose-spark.yaml build


.PHONY: compose-build