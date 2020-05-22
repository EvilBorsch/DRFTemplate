## build and run
build-and-run:
	docker rm -vf $$(docker ps -a -q) || true
	docker-compose build && docker-compose up

## run
run:
	docker rm -vf $$(docker ps -a -q) || true
	docker-compose up

#run if app runns first time
first-time:
	docker-compose run python manage.py migrate
