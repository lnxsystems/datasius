FROM nginx:latest

COPY nginx.conf /etc/nginx/
ADD  conf.d /etc/nginx/conf.d
ADD  letsencrypt /etc/letsencrypt
VOLUME ["/var/cache/nginx"]
EXPOSE 80 443

CMD ["nginx"]
