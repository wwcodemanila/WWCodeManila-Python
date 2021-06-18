##  Goals

- [ ] Starting the project
- [ ] Setting things up
- [ ] Running the server

## Starting the project

Once you've installed the `Django` web framework inside your `env` virtual environment, start the project by typing this command:
```  
django-admin startproject forumapp .
```

Your directory structure should look like this:
```
django
C:.
│   manage.py
│   requirements.txt
│
└───forumapp
        asgi.py
        settings.py
        urls.py
        wsgi.py
        __init__.py
```
These files are:

- The outer `django/` root directory is a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.
- `manage.py`: A command-line utility that lets you interact with this Django project in various ways. 
- The inner `forumapp/` directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. forumapp.urls).
- `forumapp/__init__.py`: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read [more about packages](https://docs.python.org/3/tutorial/modules.html#tut-packages) in the official Python docs.
- `forumapp/settings.py`: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
- `forumapp/urls.py`: The URL declarations for this Django project; a “table of contents” of your Django-powered site.
- `forumapp/asgi.py`: An entry-point for ASGI-compatible web servers to serve your project. See [How to deploy with ASGI](https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/) for more details.
- `forumapp/wsgi.py`: An entry-point for WSGI-compatible web servers to serve your project. See [How to deploy with WSGI](https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/) for more details.

## Setting things up

Using your favorite text editor, go to `forumapp/settings.py`. The first thing that we need to consider editing is the `TIME_ZONE`. You may get the relevant time zone in the [Wikipedia's list of time zone.](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

The code should look like this:
```
TIME_ZONE = 'Asia/Manila'
```

The second thing to check is the language. If English is not your native language, you can add this to change the default buttons and notifications from Django to be in your language.
```
LANGUAGE_CODE = 'en-us'
```

## Running the server
Once checked and ensured that the directory or the project that you are working on has the same structure stated above, run the server by typing this command:
```
python manage.py migrate 
python manage.py runserver
```

Check your browser, then go to `localhost:8000` or `http://127.0.0.1:8000/`. 

