all: build

build:
	docker build -t datasius/frontend -f Dockerfile .

run:
	docker run -d -p 8008:8008 datasius/frontend 

kill:
	docker ps | grep datasius/frontend  | cut -f 1 -d " " | xargs docker kill

