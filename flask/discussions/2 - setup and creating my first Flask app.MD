Before you begin, make sure you have [Python](https://www.python.org/downloads/) installed and ready-to-use.

## Setup and installation

### Virtual Environment

Since we will be using Flask together with several extensions, it is recommended to create a [virtual environment](https://pypi.python.org/pypi/virtualenv) to isolate our Python environment and avoid affecting our main Python installation.

`Virtualenv` is a useful tool that creates isolated Python development environments where you can do all your development work.

Open your terminal or console and check if your sytem already has `virtualenv`:

```shell
$ virtualenv --version
```

If you see a version number, that means you already have it installed and you may now skip to Flask installation. If not, install it using this:

```shell
$ easy_install virtual env
or
$ pip install virtualenv
or
$ apt-get install python-virtualenv
```

In case you don't have `easy_install` on your computer, install it by following the instructions [here](https://pypi.python.org/pypi/setuptools).

Lastly, install `virtualenvwrapper` to make working with virtual environments much more pleasant (especially for Windows users), since it also places all of your virtual environments a single location.

```shell
Mac:
$ pip install virtualenvwrapper
$ export WORKON_HOME=~/Envs
$ source /usr/local/bin/virtualenvwrapper.sh

Windows:
$ pip install virtualenvwrapper-win
```

### Flask

Once you've installed `virtualenv`, create a new isolated development environment:

```shell
mkvirtualenv HelloWorld
```

This produces a folder named `HelloWorld` with a clean copy of Python inside.

You may now begin using your newly created virtual environment by activating it:

```shell
$ workon HelloWorld
```

Once activated, install Flask through `pip`:

```shell
$ pip install Flask
```

### My First Flask Application

Now, to create a minimal Flask application, create a file named `hello.py` inside your project folder (~/Envs):

```shell
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

In your terminal or console, navigate to the location of your project folder and set the `FLASK_APP` environment variable:

```shell
Mac:
export FLASK_APP=hello.py

Windows:
set FLASK_APP=hello.py
```

Finally, run your application:

```shell
flask run
```

Congratulations! You can now access your app through the url route generated in your terminal or console using your favorite browser.

To quit, just press `CTRL+C`.

To deactivate your virtual environment, simply enter `deactivate`.