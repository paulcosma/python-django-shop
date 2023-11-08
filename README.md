# python-django
Django - a library of reusable modules (building blocks - e.g.: http requests, urls, sessions, cookies)
A framework also defines a structure for your application.

```bash
pip install django==2.1
django-admin startproject pyshop .
# python3 -m django startproject pyshop .
```
"pyshop" folder is a package (has an __init__.py) so we can import various modules from this package into other modules.
- settings = various settings for the application
- urls = module where we define what users see when they go to an url
- wsgi = web-server-gateway-interface to provide a standard interface between django and webservers

- manage.py - used to manage this django project (start webserver, work with database)

Start server
```bash
python3 manage.py runserver
```
- Open  http://127.0.0.1:8000/

- Create new App
```bash
python3 manage.py startapp products
```

- Create a View function
- Open views.py from products folder.
```bash

```
- Create the Model into DB
cUpdate pyshop/settings.py INSTALLED_APPS to include our products app 'products.apps.ProductsConfig'
```bash
python3 manage.py makemigrations
# a new file will be created in \products\migrations\0001_initial.py
# Generate produc table
python3 manage.py migrate
```
- Create the superuser
```bash
python3 manage.py createsuperuser
# enter user, password, and email
```

HTML
- "{%" - in html file is a "template tag" used to dynamically execute login (inside {% %} you can write for loops or if statements)
- "{{ }}" - use to dynamically render values in html markup

Bootstrap framework
Create base.html from https://getbootstrap.com/docs/5.3/getting-started/introduction/#quick-start

To be able to use base.html from templates directory Update pyshop/settings.py TEMPLATES = [ ... ]
```bash
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
```