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
ADD requirements.txt /srv/datasius/requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

WORKDIR /srv/datasius
ADD frontend
ADD add data
EXPOSE 8000
WORKDIR /srv/datasius/frontend
CMD  ["sh", "run.sh"]
