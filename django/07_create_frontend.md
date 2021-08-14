## Goals
- [ ] Create a Registration Link on the Login Page
- [ ] Create a Login Link on the Registration Page
- [ ] Adding Margins to Layout
- [ ] Adding a Border 

## Create a Registration Link on the Login Page
Yay! We are done setting-up the backend of our application! Now, we will be focusing on the front-end side of the app. We want to make it more `user-friendly` that is why we are going to modify or add a few things.

Open `templates/registration/login.html`. Add this line of code after `<h1>Login<h1>`:

```
<p class="lead text-muted">Share Your Knowledge!</p>
```

Also, add the registration link inside the class `login-form-container` after the `form` tag:

```
<p class="mt-2">Or <a href="{% url 'django_registration_register' %}">Create an Account</a></p>
```

The code should look like this:
```
{% extends 'auth_layout.html' %}
{% load crispy_forms_tags %}

{% block content %}
<h1>Login</h1>
<p class="lead text-muted">Share Your Knowledge!</p>
<div class="login-form-container">
    <form method="POST">
        {% csrf_token %}
        {{ form | crispy }}
        <button type="submit" class="btn btn-sm btn-outline-primary">Login</button>
    </form>
    <p class="mt-2">Or <a href="{% url 'django_registration_register' %}">Create an Account</a></p>
</div>
{% endblock %}
```

Go to url `http://localhost:8000/accounts/login/` and see the changes. 

## Create a Login Link on the Registration Page
In this part, we are going to do the same steps. In `templates/django_registration/registration_form.html`, add this code inside the class `registration-form-container`, under the `form` tag.

```
<p class="mt-2">Or <a href="{% url 'login' %}">Login</a></p>
```
The code should look like this:
```
{% extends 'auth_layout.html' %}
{% load crispy_forms_tags %}

{% block content %}
<h1>Create Your Account</h1>
<div class="registration-form-container">
    <form method="POST">
        {% csrf_token %}
        {{ form | crispy }}
        <button type="submit" class="btn btn-sm btn-outline-primary">Create Account</button>
    </form>
    <p class="mt-2">Or <a href="{% url 'login' %}">Login</a></p>
</div>
{% endblock %}
```

Then check the changes by accessing this url: `http://localhost:8000/accounts/register/`.

## Adding Margins to Layout
In this part, we are going to add some margins to our `registration` page and `login` page. 
In `templates/auth_layout.html`, add a css class called `outer-area`. The style would look as follows:
```
    .outer-area {
        margin-top: 100px;
    }
```
Then add a new div tag outside the div class `auth-box text-center`. In the newly added div tag, call the `outer-area` class. It should look like this:

```
<body>

    <div class="outer-area">
        <div class="auth-box text-center">
            {% block content %}
            {% endblock %}
        </div>
    </div>
    
</body>
```

## Adding a Border
To add a border on registration and login page, add a css class named `auth-box`. Then add these other details:
```        
.auth-box {
    border: 3px solid lightgray;
    border-radius: 10px;
    padding-top: 25px;
    padding-bottom: 25px;
    width: 600px;
    margin: auto;
}
```