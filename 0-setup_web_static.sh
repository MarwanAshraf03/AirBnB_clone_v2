#!/usr/bin/env bash
# a comment
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "OK!!" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
echo "http {
    include mime.types;

    server {
        listen 80;
        #root /var/www/html/;
        index index.nginx-debian.html;
        location /hbnb_static {
            alias /data/web_static/current/;
        }
    }
}
events {}" > /etc/nginx/nginx.conf
sudo service nginx restart
