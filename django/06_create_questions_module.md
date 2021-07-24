## Goals
- [ ] Create questions module
- [ ] Create questions and answers serializer
- [ ] Create questions views
- [ ] Create answers views
- [ ] Create detail endpoints 
- [ ] Create like endpoint

## Create `questions` module
``` 
python manage.py startapp questions
```

After starting the application, register the app in `forumapp/settings.py`
```
INSTALLED_APPS = [
    ...
    'questions'
]
```

Define the model that we will be using for the `questions` and `anwsers`. In `questions/models.py`:
```
from django.db import models
from django.conf import settings


class Question(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=240)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="questions")

    def __str__(self):
        return self.content


class Answer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 related_name="answers")
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name="votes")

    def __str__(self):
        return self.author.username
```

Then make migrations, migrate:

```
> python manage.py makemigrations
> python manage.py migrate
```

Let us also register the models that we created to `questions/admin.py`.
```
from django.contrib import admin
from questions.models import Answer, Question

admin.site.register(Answer)
admin.site.register(Question)

```

We have defined a `SlugField` in the model. A slug is a short label for something, containing only letters, numbers or hyphens. A SlugField is a field that is automatically created. In this case, we have to find a way to create it, as it also has to be unique. We are going to use `signal`, that is used with the model. 

Create the file `questions/signals.py`:
```
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from core.utils import generate_random_string
from questions.models import Question
```

Then create a `generate_random_string` function inside `core/utils.py`:
```
import random
import string

ALPHANUMERIC_CHARS = string.ascii_lowercase + string.digits
STRING_LENGTH = 6

def generate_random_string(chars=ALPHANUMERIC_CHARS, length=STRING_LENGTH):
    return "".join(random.choice(chars) for _ in range(length))
```

After that, go back to `questions/signals.py`. Add the function `add_slug_to_question`. This will also call the function that we created in `core/utils.py`
```
@receiver(pre_save, sender=Question)
def add_slug_to_question(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.content)
        random_string = generate_random_string()
        instance.slug = slug + "-" + random_string
```

Complete the setup by registering this to `questions/apps.py`.
```
from django.apps import AppConfig


class QuestionsConfig(AppConfig):
    name = 'questions'

    def ready(self):
        import questions.signals
```

And in `questions/__init__.py`, register the `QuestionsConfig`.
```
default_app_config = "questions.apps.QuestionsConfig"
```

Check that everything works fine in your terminal by typing
```
$ python manage.py shell

>>> from django.contrib.auth import get_user_model
>>> custom_user = get_user_model()
>>> u = custom_user.objects.first()
>>> u
<CustomUser: admin>
>>> from questions.models import Question
>>> q = Question.objects.create(author=u, content="First, question! Does it work?")
>>> q
<Question: First, question! Does it work?>
>>> q.slug
'first-question-does-it-work-ea8vb1'
```

## Create questions and answers serializer
In the previous part of this chapter, we created a model for `Questions` and `Answers`. Now we need to create a seralizer for them.

Create folder `questions/api` then create `serializers.py`. 
```
from rest_framework import serializers
from questions.models import Answer, Question


class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    user_has_voted = serializers.SerializerMethodField()
    question_slug = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        exclude = ["question", "voters", "updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_likes_count(self, instance):
        return instance.voters.count()

    def get_user_has_voted(self, instance):
        request = self.context.get("request")
        return instance.voters.filter(pk=request.user.pk).exists()

    def get_question_slug(self, instance):
        return instance.question.slug


class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    answers_count = serializers.SerializerMethodField()
    user_has_answered = serializers.SerializerMethodField()

    class Meta:
        model = Question
        exclude = ["updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")

    def get_answers_count(self, instance):
        return instance.answers.count()

    def get_user_has_answered(self, instance):
        request = self.context.get("request")
        return instance.answers.filter(author=request.user).exists()
```

## Create `questions` views
In this part we will create a viewset for module `questions`. It is a class-based view without method handlers such as `get` or `post`, but it provides actions such as `.list()` and `.create()`.
questions/api/views.py

```
from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from questions.api.serializers import QuestionSerializer
from questions.api.permissions import IsAuthorOrReadOnly
from questions.models import Question


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    lookup_field = 'slug'
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


```

Then we will create a `permissions.py` file in `questions/api` folder to secure the api and restrict other users from accessing the apis. We will create a class `IsAuthorOrReadOnly`.

```
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
```


In `questions/api/urls.py`, register the view. 
```
from django.urls import include, path
from rest_framework import routers, urlpatterns
from rest_framework.routers import DefaultRouter

from questions.api import views as qv

router = DefaultRouter()
router.register(r"questions", qv.QuestionViewSet)


urlpatterns = [
    path("", include(router.urls))
]
```

After that, register the `questions` url in the `forumapp/urls.py` file. Register this inside the urlpatterns.
```
    path('api/', include('questions.api.urls')),
```

Now, try the newly created api by accessing it in your browser then by typing `localhost:8000/api/questions/`. You may access the api with the question instance. You may also try to accessor update an individual questions by adding the slug value at the end of the search bar. 
```
example:
http://localhost:8000/api/questions/first-question-does-it-work-7ue6r8/
```

## Create `answers` views
In `questions/api/views.py`, we are going to create two separate views, first to let the users answer the question, and second to list all of the answers for the questions. 

```
from rest_framework import generics, viewsets 
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404


from questions.api.serializers import AnswerSerializer, QuestionSerializer
from questions.models import Answer, Question


class AnswerCreateAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        question = get_object_or_404(Question, slug=kwarg_slug)

        if question.answers.filter(author=request_user).exists():
            raise ValidationError("You have already answered this question!")
        serializer.save(author=self.request.user, question=question)
```

Then register the View to `questions/api/urls.py`
```
path("questions/<slug:slug>/answer/",
    qv.AnswerCreateAPIView.as_view(), name='answer-create')
```

Now, go back to your browser then check whether you see an answer field, like in the example below:
```
http://localhost:8000/api/questions/do-you-like-guitars-norzk0/answer/

```

Once you accessed the link in your browser, you may notice that you cannot access a list of all of the answers in each question. The next thing that we need to do is to create a view that will list them all.

In `questions/api/views.py`, create another class called `AnswerListAPIView`.

```
class AnswerListAPIView(generics.ListAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get('slug')
        return Answer.objects.filter(question__slug=kwarg_slug).order_by('-created_at')
```

Same as what we did earlier, register the view `AnswerListAPIView` to `questions/api/urls.py`.

```
path("questions/<slug:slug>/answers/",
    qv.AnswerListAPIView.as_view(), name='answer-list')
```

Perfect! Now, go back to your browser, then access this link `http://localhost:8000/api/questions/<slug_url>/answers/`. You may now check the list of the answers in each question. :tada:


## Create detail endpoint
To finish our backend setup, we need two more endpoints; one for Retrieving, Updating and Deleting answers, and one for the "like" feature.

In `questions/api/views.py`, add a class called `AnswerRUDApiView`.

```
class AnswerRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
```
Then register again in `questions/api/urls.py`.
```
path("answers/<int:pk>/",
    qv.AnswerRUDApiView.as_view(), name='answer-detail')
```
Try accessing the url `http://localhost:8000/api/questions/<slug_api>/answers/`, you can see a list of answers with id. After that, get the id, then use that id in url `http://localhost:8000/api/answers/<id>/`. You may see the details of the answer. Try also updating and deleting the answer.

## Create like endpoint
Let us now create the last endpoint - the like endpoint. 
In `questions/api/views.py`, add a class called `AnswerLikeAPIView`.
```
from rest_framework import generics, status, viewsets

from rest_framework.response import Response
from rest_framework.views import APIView


class AnswerLikeAPIView(APIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        user = request.user

        answer.voters.remove(user)
        answer.save()

        serializer_context = {'request': request}
        serializer = self.serializer_class(answer, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        user = request.user

        answer.voters.add(user)
        answer.save()

        serializer_context = {'request': request}
        serializer = self.serializer_class(answer, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)
```

Register the view in `questions/api/urls.py`.

```
path("answers/<int:pk>/like/",
    qv.AnswerLikeAPIView.as_view(), name='answer-like')
```

Access the created endpoint by typing in `http://localhost:8000/api/answers/<id>/like/`.

The last thing that we need to do is to set the pagination in `settings.py` file.
```
REST_FRAMEWORK = {
    ...
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2
}
```

