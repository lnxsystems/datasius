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
pip install -r website/requirements.txt
cd website
python manage.py runserver
```
The above command sequence will run the development server and serve the website on localhost. Browse to http://127.0.0.1:8000/

At this point you will have the website up and running at http://127.0.0.1:8000/ . It will be running in its own development web server. For production purposes we will not be using this but only use it during development. You may edit the python code and it will automatically reload thus speeding up development. 

The source code for the frontend website is in website/website

### Website Design and Templates

The original source html templates are served via http://<ip or domain>:8000/static/master and this corresponds to the directory path website/webiste/static/master 
  
TODO: Add a description where the css , js, and which templates are used for each URL location.
## Code Layout

The website is a django app called "website". This is located in website/ and mostly inside webiste/website. 


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

using docker-compose command will allow to build and deploy the two docker containers and also populate the shared volume used to share files between the two docker instances. 

### Setup 

If you have not yet done the development setup then the following commands are required:

```
git clone git@github.com:jnvilo/datasius.git
cd datasius
sh scripts/setup-venv.sh 
source venv/bin/activate
pip install -r website/requirements.txt
```

### Build the images using docker-compose

```
docker-compose build
```
### Deploy the images using docker-compose

```
docker-compose up 
```
The above command deploys and maps port 80 to all interfaces. You can now browse and test the website via http://your_up/ 

### Stop the containers

```
docker-compose down
```


