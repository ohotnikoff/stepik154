sudo unlink /etc/nginx/sites-enabled/default
sudo ﻿ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo ln -s /home/box/web/etc/gunicorn-wsgi.conf  /etc/gunicorn.d/test
# sudo ln -s /home/box/web/etc/gunicorn-django.conf  /etc/gunicorn.d/django.conf
sudo /etc/init.d/nginx restart
