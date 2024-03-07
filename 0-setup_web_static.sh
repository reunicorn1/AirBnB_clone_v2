#!/usr/bin/env bash
# This script prepares web servers for the deployment of web_static
# installing nginx if it's not installed already
[[ ! $(dpkg-query -W nginx) ]] > /dev/null 2>&1 && sudo apt update && sudo apt install nginx -y
# create files and folders
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
# create static files and modify configuration file
echo "Hello World!" | sudo tee /var/www/html/index.html > /dev/null
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null
# creation of the symbolic link
sudo ln -s --force /data/web_static/releases/test/ /data/web_static/current
# provide ownership recursively 
sudo chown -R ubuntu:ubuntu /data/
#modify configuration file
new_string="server_name _;\n        location /redirect_me {\n                rewrite ^/redirect_me/?$ https://www.youtube.com/watch?v=dQw4w9WgXcQ permanent;\n        }"
sudo sed -i "s#server_name _;#$new_string#" /etc/nginx/sites-available/default
text="location /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "/^\tlocation \/ {/i\\ \t$text" /etc/nginx/sites-available/default
sudo service nginx restart
