from alpine:latest
MAINTAINER Jason Viloria <jnvilo@gmail.com> 

RUN apk update
RUN apk add --no-cache python3 \
    py3-tz \
    py3-gunicorn \
    ca-certificates \
    build-base \
    zlib-dev  \ 
    zlib \ 
    jpeg-dev \ 
    py3-pillow \ 
   python3-dev \
   freetype-dev \ 
   freetype \
   libjpeg-turbo-dev \
   libjpeg-turbo \
   tiff \
   tiff-dev \
   libwebp-dev \
   libwebp \
   libffi-dev \
     
&& pip3 install -U pip
ADD requirements.txt /srv/datasius/website/requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r /srv/datasius/website/requirements.txt

WORKDIR /srv/datasius/website
ADD website website
ADD data data
ADD manage.py manage.py 
ADD run.sh run.sh
EXPOSE 8008
WORKDIR /srv/datasius/website
CMD  ["sh", "/srv/datasius/website/run.sh"]
