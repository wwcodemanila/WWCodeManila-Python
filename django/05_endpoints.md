## Goals
- [ ] Create a homepage endpoint
- [ ] Create endpoints for users module

## Create a homepage endpoint
We are now going to create our endpoint. Endpoints provide a useful information about the user that is currently connected to the application. 

We saw in the `settings.py` file that the URLs are set to these. Now, we are going to create a path that points to homepage('/') and link a view to render the template. 
```
LOGIN_REDIRECT_URL = '/'
```

Create a folder in the root directory called `core`. Inside the folder create `__init__.py` and `views.py`. Inside the view, add this script.
```
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
 
 
class IndexTemplateView(LoginRequiredMixin, TemplateView):
 
    # overwrite the method
    def get_template_names(self):
        template_name = 'index.html'
        return template_name
```
We have the the `template_name` to `index.html`, but we don't have it yet, so we are going to create it inside the folder `templates`. 
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forum App</title>
</head>
<body>

    <h1> Vue JS </h1>

    <div id="app"></div>
    
</body>
</html>
```

Create a path for the class `IndexTemplateView`. Import it inside the `forumapp/urls.py`.

```
from core.views import IndexTemplateView

# Put this at the end of the urlpatterns
re_path(r"^.*$", IndexTemplateView.as_view(), name='entry-point'),
```

Check again your browser, then go to `localhost:8000` or `http://127.0.0.1:8000/`. You should be seeing Vue JS text.

## Create endpoints for users module
We will continue creating endpoints for the users module. Create the folder `api` in `users` module. Inside it, create the ff folders:
```
- serializers.py
- urls.py
- views.py
```

Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes, then rendered to `JSON`, or `XML`. 

In `users/api/serializers.py`, add this set of code:
```
from rest_framework import serializers
from users.models import CustomUser


class UserDisplaySerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["username"]
```

The view function, takes a web request and returns a web response. It is important to know that views handles the logic that gets processed each time a different URL is visited.

In `users/api/views.py`, add this block of code:

```
from rest_framework.response import Response
from rest_framework.views import APIView
from users.api.serializers import UserDisplaySerializer


class CurrentUserAPIView(APIView):

    def get(self, request):
        serializer = UserDisplaySerializer(request.user)
        return Response(serializer.data)
```

We need to ensure that our created view is registered in `users/api/urls.py`.
```
from django.urls import path
from users.api.views import CurrentUserAPIView

urlpatterns = [
    path("user/", CurrentUserAPIView.as_view(), name="current-user")
]
```

And in `forumapp/urls.py`, register the api under users.
```
    path("api/", include("users.api.urls")),
```

Again reload and check your browser! Access this URL:
`localhost:8000/api/user/`

As you can see in the browser, the `username` is shown. It is because of what we did earlier in the serializer and view.


