all: build

build:
	docker build -t datasius/frontend -f Dockerfile.frontend .
