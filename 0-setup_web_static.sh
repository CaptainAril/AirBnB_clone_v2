#!/usr/bin/env bash
# Installs and configures NginX  on a remote server
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo ufw allow 'NginX HTTP'
sudo chmod -R 777 /var/www/html
sudo chmod -R 777 /usr/share/nginx/html
sudo chmod -R 777 /etc/nginx/sites-available/default
echo 'Hello World!' > /var/www/html/index.html
echo "Ceci n'est pas une page" > /usr/share/nginx/html/custom_404.html
sudo chmod -R 755 /var/www/html
sudo chmod -R 755 /usr/share/nginx/html
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo chmod -R 777 /data
HTML=\
"<html>
	<head>
	</head>
	<body>
		Holberton School
        </body>
</html>
"
echo -e "$HTML" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chmod -R 755 /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
config=\
"server {
	listen 80 default_server;
	listen [::]:80 default_server;
	add_header X-Served-By \$HOSTNAME;
	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	server_name _;
	rewrite ^/redirect_me https://youtube.com permanent;
	location / {
		 try_files \$uri \$uri/ =404;
        }
	location /hbnb_static {
		 alias /data/web_static/current/;
        }
	error_page 404 /custom_404.html;
	location = /custom_404.html {
		 root /usr/share/nginx/html;
		 internal;
        }
}"
echo -e "$config" > /etc/nginx/sites-available/default
sudo chmod -R 755 /etc/nginx/sites-available/default
sudo nginx -t
sudo service nginx restart

