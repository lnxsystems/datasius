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
     
&& pip3 install -U pip
ADD requirements.txt /srv/datasius/frontend/requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r /srv/datasius/frontend/requirements.txt

WORKDIR /srv/datasius/frontend
ADD frontend frontend
ADD data data
ADD scripts scripts
EXPOSE 8008
WORKDIR /srv/datasius/frontend
CMD  ["sh", "/srv/datasius/scripts/run.sh"]
