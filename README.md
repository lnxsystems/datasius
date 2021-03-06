# datasius
Datasius FrontEnd Website development.

## Development Setup

This setup was only tested on Fedora 31.

To develop, either pull from this repository or fork it and pull

```
git clone --recurse-submodules --remote-submodules git@github.com:jnvilo/datasius.git
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

As a convenience, the original source html templates are served via http://<ip or domain>:8000/static/master and this corresponds to the directory path website/webiste/static/master. This is usefull to check out the original master html templates. 

TODO: Add a description where the css , js, and which templates are used for each URL location.
## Code Layout

The website is a django app called "website". This is located in website/ and mostly inside webiste/website.


## Docker

**If you just want to launch the docker images for website and the nginx frontend, skip down to docker-compose.**


### frontend website Dockerfile

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

## Registration

The registration process is a multi step process.


### /accounts/register/
The user first reaches a web page where he/she can fill up the registration form.

The template for this page can be found in website/static/templates/django_registration/registration_form.html

### registraion completed

After the user fills in the form and clicks register, he is sent to the registration completed page.

The template for this page is: website/static/templates/django_registration/registration_complete


This page tells the user that his account has been created but not yet activated. And that
he should check his email and click on the activation link.

### Email to the user

At the same time after the user clicks submit on the registration form, he is sent an email. This
email is created from two templates which are

* website/static/templates/django_registration/activation_email_body.txt
* website/static/templates/django_registration/subject.txt

### Activation complete

Once the user clicks on his activation email he will be redirected to the activation_complete page.

Template for this is at: website/static/templates/django_registration/activation_complete.html





