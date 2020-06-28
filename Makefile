.PHONY: run-dev-db
run-dev-db:
	docker-compose up -d dev-database

.PHONY: restart-dev-db
restart-dev-db: |
	-container_id=$$(eval docker ps -aqf "name=dev-database") \
	docker kill $$container_id \
	docker rm $$container_id
	docker-compose up -d dev-database
	pipenv run python manage.py loaddata seed_data.json


.PHONY: migrate-database
migrate-database: |
	pipenv run python manage.py migrate

.PHONY: serve
serve:
	pipenv run python manage.py runserver