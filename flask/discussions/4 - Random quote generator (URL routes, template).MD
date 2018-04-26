# Creating a Random Quote Generator Web App

Let's create a simple random quote generator web app using Flask!

![Random quote generator](https://pythonspot-9329.kxcdn.com/wp-content/uploads/2015/03/python-flask-webap.png)


## First step: Create your development environment

Create a new isolated development environment for our new project and activate it.

```shell
$ mkvirtualenv QuoteSearchEngine
$ workon QuoteSearchEngine
```

Once activated, install Flask through pip:

```shell
$ pip install Flask
```

Go inside your `QuoteSearchEngine` and create our project folder named `app`

```shell
$ cd QuotesSearchEngine
$ mkdir app
$ cd app
```

## Second step: Create your URL routes

Decide the url routes for your web application. We can use the following:

```shell
/
/hello/<name>
```

Under your project folder, create a file called `hello.py`

```python
from flask import Flask

app = Flask(__name__)
 
@app.route("/")
def index():
    return "My Flask homepage!"

    
@app.route("/hello/<string:name>/")
def hello(name):
    return "Hello" + name
```

Run your application and try these URLs in your browser:

```shell
http://127.0.0.1:5000/
http://127.0.0.1:5000/hello
http://127.0.0.1:5000/hello/your_name
http://127.0.0.1:5000/hello/your_name/
```

## Third step: Create your templates

Create your templates folder and copy the [templates](https://github.com/wwcodemanila/WWCodeManila-Python/tree/master/flask/assets) 
for `hello.html` and `layout.html`. As challenge, you can separate further the style to its own stylesheet file.

Update your `hello` function to use the template.

```python
from flask import Flask

app = Flask(__name__)
 
@app.route("/")
def index():
    return "My Flask homepage!"
    
@app.route("/hello/<string:name>/")
def hello(name):
    # UDPATE NEEDED
    return render_template('test.html')
```

Restart the app!

![Random quote generator](https://pythonspot-9329.kxcdn.com/wp-content/uploads/2015/03/python-webapp-flask.png.webp)


## Fourth step: Randomize your quotes!

Our random quote generator is not so-so random because of the hardcoded quote on our `hello.html` file.

```html
<p>
    <!-- UPDATE NEEDED -->
    "The limits of my language are the limits of my mind. All I know is what I have words for."
</p>
```

Aside from the name variable, we will also need to pass a quote variable and change your `hello.html` to
show the quote variable's value.

Update your `app.py` to get a random quote from a list of quotes!

```python
from flask import Flask

app = Flask(__name__)
 
@app.route("/")
def index():
    return "My Flask homepage!"
    
@app.route("/hello/<string:name>/")
def hello(name):
    quotes = [
        "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
        "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
        "'To understand recursion you must first understand recursion..' -- Unknown",
        "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
        "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
        "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"
        ]
    # UPDATE NEEDED: Get random index from quotes
    # randomNumber = 
    # quote = 
    return render_template('test.html')
```

Restart the app and check if your random quote is not faking it!

![Random quote generator](https://pythonspot-9329.kxcdn.com/wp-content/uploads/2015/03/python-flask-webap.png.webp)


### Getting crazy? Need help?
If you have questions, please feel free to ask and participate on our [Gitter group](https://gitter.im/WWCodeManila/Python).


### References
*  [Tutorial](https://pythonspot.com/en/flask-web-app-with-python/)
*  [Slides](https://docs.google.com/presentation/d/1yWr0I2aU0tFMMeQ4s4cUcv0V1Mxq1CmCPdkP-V1atlg/edit?usp=sharing)