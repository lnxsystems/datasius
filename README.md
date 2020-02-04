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
cd frontend
python manage.py runserver
```

At this point you will have the website up and running at http://127.0.0.1:8000/

The source code for the frontend website is in datasius/frontend


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
