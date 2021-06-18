## Goals
- [ ] Create questions module
- [ ] Create questions and answers serializer

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