# datasius
Datasius FrontEnd Website development. 

## Development Setup 

This setup was only tested on Fedora 31. 

To develop, either pull from this repository or fork it and pull 

```
git clone git@github.com:jnvilo/datasius.git
cd datasius
sh scripts/setup-venv.sh 
source venv/bin/activate
cd website
python manage.py runserver
```

At this point you will have the website up and running at http://127.0.0.1:8000/ . It will be running in its own development web server. For production purposes we will not be using this but only use it during development. You may edit the python code and it will automatically reload thus speeding up development. 

The source code for the frontend website is in website/website

## Docker 

To build the docker image for the website.

### Working on frontend website Dockerfile

The following commands assumes you are inside the datasius root directory.
```
cd website
docker build -t datasius/website . 
```

During development, you can enter the docker image or container with the following commands:

```
docker run -it datasius/website /bin/sh   #Create a container and execute /bin/sh
docker exec -it <container_id_or_name> /bin/sh #To enter a running container.
```
### Working on nginx Dockerfile

```
cd nginx
docker build -t datasius/nginx . 
```

## Docker-Compose

The website is composed of two docker images. 

* datasius/frontend
* datasius/nginx

The Nginx proxy also serves all static file from the website docker image. All static files are copied into the shared volume. /srv/datasius/static-root. During development there is no need to copy these files. All static files should be placed inside website/website/static.

### Using the Makefile

There is a makefile that can be used to build and run the docker image during development. 


## Dev tasks

### Initial
1. Setup database to be in ../frontend/frontent/data

### Registration
1. install django-registration
1.1 Create 2 step activation with email 
1.2 Create basic templates for each page. 

### Templates:
1. Allow viewing of static sample files.


### Deployment

1.1 Create docker instance for website
1.2 Create nginx frontend
1.3 deploy using docker-compose 


### Dev Setup Tasks

1.1 Create a setup script to create the dev environment. 

### Nginx Proxy Setup

1.1 Create docker nginx 
1.2 Setup static files to be served by nginx
