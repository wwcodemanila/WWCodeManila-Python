## Goals
- [ ] Additional setup
- [ ] Add navbar component
- [ ] Initialize csrf token 
- [ ] Add home component and questions list
- [ ] Add single question component

## Additional Setup
Add this script to be shown whenever there is an error with JavaScript in `templates/index.html`, above the div id app.
```
    <noscript>
        <strong>We're sorry but frontend doesn't work properly without JavaScript enabled. Please enable it to continue.</strong>
    </noscript>
```

Comment out the base key-value in `src/router/index.js`, `const router`. This will remove the extended baseurl that we saw in our browser.
```
const router = new VueRouter({
  mode: "history",
  // base: process.env.BASE_URL,
  routes,
});
```

## Add navbar component
Now, we are going to create a navbar component to our application. 

New file `templates/base.html`. Code should be like this.
```
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Forum Application</title>
        <!-- Get the bootstrap tag at getbootstrap.com -->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css" integrity="sha384-B0vP5xmATw1+K9KRQjQERJvTumQW0nPEzvF6L/Z6nronJ3oUOFUFpCjEUQouq2+l" crossorigin="anonymous">
        {% block style %}
        {% endblock %}
    </head>
    <body>

        {% block content %}
        {% endblock %}

    </body>
</html>
```

Change the `auth-layout` page to this:
```
{% extends "base.html" %}
{% block style %}
<style>
    .login-form-container {
        width: 300px;
        margin: auto;
    }
    .registration-form-container {
        width: 400px;
        margin: auto;
    }
    .outer-area {
        margin-top: 100px;
    }
    .auth-box {
        border: 3px solid lightgray;
        border-radius: 10px;
        padding-top: 25px;
        padding-bottom: 25px;
        width: 600px;
        margin: auto;
    }
</style>
{% endblock %}


{% block content %}
<div class="outer-area">
    <div class="auth-box text-center">
        {% block auth %}
        {% endblock %}
    </div>
</div>
{% endblock %}
```

As you can see here in the code, it has several blocks called liquid tags. It basically helps to override the specific parts of the template. 

Now, we should change some block names in files `templates/django_registration/registration_form.html` and `templates/registration/login.html`. 
```
{% block auth %}
    ...
{% endblock %}
```

We should add add an import of the `auth-layout` to the same files mentioned. This should be added on the first line of the code.
```
{% extends 'auth_layout.html' %}
```

Now we are going to add a file `frontend/src/components/Navbar.vue` to add the navigation bar. 
```
<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
        <div class="container">
            <router-link
                :to="{ name: 'home' }"
                class="navbar-brand"
            >Forum Application
            </router-link>

            <div class="collapse navbar-collapse">
                <ul class="navbar-nav ml-auto">
                <li class="nav-item active">
                    <router-link
                        :to="{ name: 'Home' }"
                        class="btn btn-sm btn-success"
                    >Home
                    </router-link>
                </li>
                <li class="nav-item mx-2">
                    <router-link
                        :to="{ name: 'Home' }"
                        class="btn btn-sm btn-danger"
                    >Add Question
                    </router-link>
                </li>
                <li class="nav-item">
                    <a class="btn btn-sm btn-outline-secondary" href="/accounts/logout/">Logout</a>
                </li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script>
export default {
    name: "NavbarComponent"
}
</script>

<style>
    .my-navbar {
        border-bottom: 1px solid #DDD;
    }

    .navbar-brand {
        font-weight: bold;
        font-size: 130%;
    }

    .navbar-brand:hover {
        color: #DC3545 !important;
    }
</style>
```

Then, import this navbar component in `frontend/src/App.vue`. Under the template tag, add a new tag called script.
```
<script>
import NavbarComponent from "./components/Navbar.vue"
export default {
  name: "App",
  components: {
    NavbarComponent
  }
}
</script>
```

Remove the following as it is no longer needed
```
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
```

Then, replace it with `<NavbarComponent />`. The code should look like this:
```
<template>
  <div id="app">
    <NavbarComponent />
    <router-view />
  </div>
</template>

<script>
import NavbarComponent from "./components/Navbar.vue"
export default {
  name: "App",
  components: {
    NavbarComponent
  }
}
</script>

<style>
    html, body {
        height: 100%;
        font-family: Avenir, Helvetica, Arial, sans-serif;
    }

    .btn:focus {
      box-shadow: none !important;
    }
</style>
```

Check the changes in your broswer! 

Let's add a container in our html code in `frontend/src/views/Home.vue`.
```
    <div class="container"> 
      <img alt="Vue logo" src="../assets/logo.png" />
      <HelloWorld msg="Welcome to Your Vue.js App" />
    </div>
```

## Initialize csrf token
In `frontend` folder, create a folder named `common`. Add two files named `csrf_token.js` and `api.service.js`

Add this script in `csrf_token.js`.
```
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const CSRF_TOKEN = getCookie('csrftoken');

export { CSRF_TOKEN };
```

On the other hand, add this script inside `api.service.js`. 
```
import { CSRF_TOKEN } from "./csrf_token.js"

async function getJSON(response) {
    if (response.status === 204) return '';
    return response.json()
}

function apiService(endpoint, method, data) {
    const config = {
        method: method || "GET",
        body: data !== undefined ? JSON.stringify(data) : null,
        headers: {
            'content-type': 'application/json',
            'X-CSRFTOKEN': CSRF_TOKEN
        }
    };
    return fetch(endpoint, config)
            .then(getJSON)
            .catch(error => console.log(error))
}

export { apiService };
```

Then remove the VueJS logo by deleting or commenting this line of code in file `frontend/src/views/Home.vue`
```
    <img alt="Vue logo" src="../assets/logo.png" />
```

## Add home component and questions list
Let's do a little bit of cleanup. Delete this code in `frontend/src/views/Home.vue`
```
    <!-- <img alt="Vue logo" src="../assets/logo.png" /> -->
    <HelloWorld msg="Welcome to Your Vue.js App" />
```

In `frontend/src/views/Home.vue`, import apiService
```
<script>
import { apiService } from "../common/api.service"
export default {
    name: "home",
    data() {
        return {
            questions: []
        }
    },
    methods: {
        getQuestions() {
            let endpoint = "/api/questions/";
            apiService(endpoint)
              .then(data => {
                  this.questions.push(...data.results)
              })
        }
    },
    created() {
        this.getQuestions()
    }
}
```

Still in `frontend/src/views/Home.vue`, populate the fields by the data given from the endpoint.
```
<template>
  <div class="home">
    <div class="container"> 
      <div v-for="question in questions"
        :key="question.pk">
        <p class="mb-0">Posted by:
            <span class="author-name">{{ question.author }}</span>
        </p>
        <h2> {{ question.content }} <h2>
        <p>Answers: {{ question.answers_count }}<p>
        <hr>
      </div>
    </div>
  </div>
</template>
```

And add style for the author name.
```
<style>
  .author-name {
    font-weight: bold;
    color: #DC3545;
  }
</style>
```


## Add single question component
Add `Question.vue` in views folder. 
```
<template>
    <div class="single-question mt-2">
        <div class="container">
            <h1>{{ question.content }}</h1>
            <p class="mb-0">Posted by:
                <span class="author-name">{{ question.author }}</span>
            </p>
        </div>
    </div>
</template>

<script>
import { apiService } from "../common/api.service.js"
export default {
    name: "Question",
    props: {
        slug: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            question: {}
        }
    },
    methods: {
      getQuestionData() {
          let endpoint = '/api/questions/${this.slug}/';
          apiService(endpoint)
            .then(data => {
                this.question = data;
            })
      }
    },
    created() {
        this.getQuestionData()
    }
}
</script>

<style scoped>
  .question-author {
    font-weight: bold;
    color: #DC3545;
  }
  .question-link {
    font-weight: bold;
    color: black;
  }
  .question-link:hover {
    color: #343A40;
    text-decoration: none;
  }
</style>
```

Import the Questions.vue file to `frontend/src/router/index.js`. 
```
import Question from "../views/Question.vue";
...

  {
    path: "/question/:slug",
    name: "question",
    component: Question,
    props: true
  },
```

Then add another router-link in `frontend/src/views/Home.vue`. Add also a style for the question link class.
```
<h2> 
    <router-link
    :to="{ name: 'question', params: { slug: question.slug } }"
    class="question-link"
    >{{ question.content }}
    </router-link>
</h2>
```
```
<style scoped>
  .question-author {
    font-weight: bold;
    color: #DC3545;
  }
  .question-link {
    font-weight: bold;
    color: black;
  }
  .question-link:hover {
    color: #343A40;
    text-decoration: none;
  }
</style>
```

After the changes, the file `frontend/src/views/Home.vue` should look like this:
```
<template>
  <div class="home">
    <div class="container"> 
      <div v-for="question in questions"
        :key="question.pk">
        <p class="mb-0">Posted by:
            <span class="question-author">{{ question.author }}</span>
        </p>
        <h2> 
          <router-link
            :to="{ name: 'question', params: { slug: question.slug } }"
            class="question-link"
          >{{ question.content }}
          </router-link>
        </h2>
        <p>Answers: {{ question.answers_count }}<p>
        <hr>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "../common/api.service.js"
export default {
    name: "home",
    data() {
        return {
            questions: []
        }
    },
    methods: {
        getQuestions() {
            let endpoint = "/api/questions/";
            apiService(endpoint)
              .then(data => {
                  this.questions.push(...data.results)
              })
        }
    },
    created() {
        this.getQuestions()
        console.log(this.questions);
    }
}
</script>

<style scoped>
  .question-author {
    font-weight: bold;
    color: #DC3545;
  }
  .question-link {
    font-weight: bold;
    color: black;
  }
  .question-link:hover {
    color: #343A40;
    text-decoration: none;
  }
</style>
```


