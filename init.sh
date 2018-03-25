sudo unlink /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn-wsgi.conf  /etc/gunicorn.d/wsgi
sudo ln -s /home/box/web/etc/gunicorn-django.conf  /etc/gunicorn.d/django
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start
mysql -uroot -e "create database ask"
git config --global user.email "ohotnikoff@bk.ru"
git config --global user.name "ohotnikoff"