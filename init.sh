sudo pip install --upgrade django
sudo pip install --upgrade gunicorn

sudo unlink /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo ln -s /home/box/web/etc/gunicorn-wsgi.conf  /etc/gunicorn.d/wsgi.conf
sudo ln -s /home/box/web/etc/gunicorn-django.conf  /etc/gunicorn.d/django.conf
sudo /etc/init.d/nginx restart
sudo gunicorn -c /home/box/web/etc/gunicorn-wsgi.conf hello:app
sudo gunicorn -c /home/box/web/etc/gunicorn-django.conf ask.wsgi:application
