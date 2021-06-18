## Goals
- [ ] Create users module
  - [ ] Adding a model
  - [ ] Registering users module to admin
- [ ] Application Settings
- [ ] Create a superuser
- [ ] Install other required libraries
- [ ] Adding to urls
- [ ] Settings and Templates

## Create `users` module
``` 
python manage.py startapp users
```

```
django
C:.
│   manage.py
│   requirements.txt
│
├───forumapp
│   │   asgi.py
│   │   settings.py
│   │   urls.py
│   │   wsgi.py
│   |____init__.py
│
└───users
    │   admin.py
    │   apps.py
    │   models.py
    │   tests.py
    │   views.py
    │   __init__.py
    │
    └───migrations
            __init__.py
```

In order to use the newly-created module (`users`), and the library `rest_framework`,
add them to the file `settings.py`. `rest_framework.authtoken` should also be added for token authentication.
```
INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'users'
] 
```
### Adding a model
We are not going to add new fields to the model, but it is also a good idea to think about the future of the project. We are going to use the User model of django.
Go to `users/models.py`, enter this command:
```
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass
```

The user model is important for the authentication. We need to explicitly state that we're using a custom model. In `settings.py`, add this at the end:
```
AUTH_USER_MODEL = "users.CustomUser"
```

### Registering users module to admin
Add the custom model user. Go to `users/admin.py`, enter this command:
```
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["username", "email", "is_staff"]


admin.site.register(CustomUser, CustomUserAdmin)
```

Then make migrations, migrate:

```
> python manage.py makemigrations
> python manage.py migrate
```

## Create a superuser

Now, we already have the users module, but we don't have an actual `user`. What are we going to do is to create a `superuser`. 

```
python manage.py createsuperuser
```

Enter your information and press enter.

```
Username: admin123
Email address: admin123@example.com
Password: admin123
Password (again): admin123
Superuser created successfully.
```

Now, let's run again the server.

``` 
python manage.py runserver
```

Access the admin interface by entering this url in your browser:
```
http://localhost:8000/admin
```

## Install other required libraries
We need to enable creation of new accounts and authenticate them, so we will be needing a couple of packages in our project.
```
pip install django-rest-auth django-allauth django-registration django-crispy-forms
pip freeze > requirements.txt
```

- django-rest-auth enables user registration with activation, login/logout, etc.
- django-allauth enables signup of both local and social accounts
- django-registration enables two-phase(with confirmation email)/one-phase(immediately active and logged in)registration
- django-crispy-forms used to create good looking forms

We also need to activate our installed libraries in `settings.py`:
```
'django.contrib.sites'
'allauth',
'allauth.account',
'allauth.socialaccount',
'rest_auth',
'rest_auth.registration'
 
'crispy_forms'
```

Next is setting important variables to the libraries the we added. 
```
# Custom User Model
AUTH_USER_MODEL= 'users.CustomUser'

# django-crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# django.contrib.sites
SITE_ID = 1

# django.allauth
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_EMAIL_REQUIRED = (True)
```

Then make migrations, migrate:

```
> python manage.py makemigrations
> python manage.py migrate
```

## Adding to urls
Add new urls to our application. In `forumapp/urls.py`:
```
from django.urls import include, path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login and registration paths provided by django
    path('accounts/', include('django.contrib.auth.urls')),

    # Login via browsable API
    path('api-auth/', include('rest_framework.urls')),

    # Login via rest
    path('api/rest-auth/', include('rest_auth.urls')),

    # Registration via rest
    path('api/rest-auth/registration/', include('rest_auth.registration.urls')),

]
```

We are going to use the views provided by the Django registration package, even though those views expect us to use a default user model. Since we are using a custom user, we also need to create a custom form.

In users folder, create `forms.py`. Also enter this script:
```
from django_registration.forms import RegistrationForm
from users.models import CustomUser
 
 
class CustomUserForm(Registration Form):
 
    class Meta(RegistrationForm.Meta):
        model = CustomUser
```

Now, import the file to `forumapp/urls.py`.
```
# Skip email verification
from django_registration.backends.one_step.views import RegistrationView
 
from users.forms import CustomUserForm

# Custom version of the registration provided by django registration
path('accounts/register/', 
        RegistrationView.as_view(
            form_class=CustomUserForm,
            success_url = '/',
        ), name='django_registration_register'),

# Other URLs provided by django registration package
path('accounts/', include('django_registration.backends.one_step.urls')),
```
For more info about RegistrationView, go to this [link.](https://django-registration.readthedocs.io/en/3.1.2/one-step-workflow.html)


After that, go to `settings.py`, add the following. This will help us redirect after logging in, logging out. 
```
LOGIN_URL = 'accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```

## Settings and Templates
The next step that we are going to do is to create templates that are needed to authenticate users via browser. 

Go to `forumapp/settings.py`, set this command:
```
# Django-REST-Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}
```

Then create a templates directory. Still inside the `settings.py` file, add the directory inside the dictionary `TEMPLATES` like this. Also add the templates folder in the root directory. 
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # this should be added 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

Inside the templates folder, add two more folders: `django_registration` `registration`.

- `django_registration` - to cater the templates required by Django Registration package.
- `registration` - store all the login related templates used by Django.

Now, we have to make sure that the authetication-related templates share a common layout. Let's create a new file called `templates/auth_layout.html`. 
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Get the bootstrap tag at getbootstrap.com -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css" integrity="sha384-B0vP5xmATw1+K9KRQjQERJvTumQW0nPEzvF6L/Z6nronJ3oUOFUFpCjEUQouq2+l" crossorigin="anonymous">
    <title>Forum App</title>
</head>
<body>
 
    <div class = "auth-box text-center">
        {% block content %}
        {% endblock %}
    </div>
    
</body>
</html>
```

We can add a new template called `templates/registration/login.html`. This html file will call the main design `auth_layout`, then add new style such as the login form container. 
```
{% extends 'auth_layout.html' %}
{% load crispy_forms_tags %} 

{% block content %}
<h1>Login</h1>
<div class = "login-form-container">
    <form method="POST">
        {% csrf_token %}
        {{ form | crispy }}
        <button type="submit" class="btn btn-sm btn-outline-primary">Login</button>
    </form>
</div>
{% endblock %}
```

Now, let's define the style `login-form-container` in `templates/auth_layout.html`. The style tag should be inside the `<head>` tag.
```
    <style>
        .login-form-container {
            width:300px;
            margin: auto;
        }
    </style>
```

Next is to create a template called `templates/django_registration/registration_form.html`. Just copy from `templates/registration/login.html`, then change necessary information.
```
{% extends 'auth_layout.html' %}
{% load crispy_forms_tags %}
 
{% block content %}
<h3>Create your Account</h3>
<div class = "registration-form-container">
    <form method="POST">
        {% csrf_token %}
        {{ form|crispy }}
        <button type="submit" class="btn btn-sm btn-outline-primary">Create Account</button>
    </form>
</div>
{% endblock %}
```

Don't forget also to add the style in `templates/auth_layout.html`.
```
    <style>
        .registration-form-container {
            width:400px;
            margin: auto;
        }
    </style>
```

Now reload, then check your browser! Access this URL:
`localhost:8000/accounts/register`