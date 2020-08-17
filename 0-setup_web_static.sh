#!/usr/bin/env bash
#This scirpt sets up the web server for deployment

#install nginx
sudo apt-get -y update
sudo apt-get -y install nginx

#Creating directories
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

#Creating index test
echo "Holberton School" > /data/web_static/releases/test/index.html

#simbolic link 
sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current 

#ownership and group
sudo chown -R ubuntu:ubuntu /data/

#routing to web static
sudo sed -i "s/server_name _;/server_name _;\n\n\tlocation \/hbnb_static\/ {\n\t\t alias \/data\/web_static\/current\/;\n\t}/" /etc/nginx/sites-available/default

#restart nginx
sudo service nginx restart
