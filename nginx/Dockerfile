FROM nginx:latest

COPY nginx.conf /etc/nginx/
ADD  conf.d /etc/nginx/conf.d
ADD  letsencrypt /etc/letsencrypt
COPY www.lnxsystems.com /srv/www.lnxsystems.com
VOLUME ["/var/cache/nginx"]
EXPOSE 80 443

CMD ["nginx"]
