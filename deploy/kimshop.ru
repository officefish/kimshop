<VirtualHost *:80>
    ServerName www.kimshop.ru
    ServerAlias kimshop.ru *.kimshop.ru
    ServerAdmin admin@obereg.com

    WSGIScriptAlias / /www/django/kimshop/kimshop/wsgi.py
    #Alias /static/blog/ /www/django/blogondjango/blog/static/blog/
    #Alias /static/ /www/django/simpleboard/simpleboard/static/
</VirtualHost>