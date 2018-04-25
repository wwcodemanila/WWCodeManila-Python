Before you begin, make sure you have [Python](https://www.python.org/downloads/) installed and ready-to-use.

###  Prerequisites

- [ ] Understand the importance of virtual environment
- [ ] Install and create a virtual environment
- [ ] Install and use `virtualenvwrapper`
- [ ] Create and run a simple Flask application

![Simple Flask application](https://pythonspot-9329.kxcdn.com/wp-content/uploads/2015/03/python-flask-webapp.png)

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

### Getting crazy? Need help?
If you have questions, please feel free to ask and participate on our [Gitter group](https://gitter.im/WWCodeManila/Python).