##  Goals

- [ ] Understand the importance of virtual environments
- [ ] Install and create a virtual environment
- [ ] Install and use `virtualenvwrapper`
- [ ] Install Flask through pip

## Virtual Environments

A **virtual environment** is a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages. It is used to isolate a particular project to avoid conflicts with the requirements of another project. **`virtualenv`** is a tool used to create Python virtual environments.

## Installing 'virtualenv'

Check if `virtualenv` already exists in your system through your terminal or console:

```shell
$ virtualenv --version
```

If you see a version number, that means you already have it installed and may now proceed to the next step. Otherwise, install `virtualenv` through the Python package manager, a.k.a. `pip`:

```shell
$ pip install virtualenv
```

Visit this [link](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/) for more info on how to make sure you have the latest version of pip installed.

## Working with 'virtualenv'

To create a virtual environment, go to your project's directory and run `virtualenv`:

```shell
cd path/to/directory
virtualenv env
```

The second argument refers to the location where you want to create the `virtualenv`. Generally, you can just create this in your project and call it `env`. `virtualenv` will create a virtual Python installation in the `env` folder.

**Note**: Don't forget to exclude your `virtualenv` directory from your version control system using .gitignore or similar.

To activate your `virtualenv`:

```shell
Windows
$ .\env\Scripts\activate

Linux and macOS
$ source env/bin/activate
```

To confirm if you're in the `virtualenv` by checking the location of your Python interpreter, which should point to the `env` directory:

```shell
Windows
$ where python

Linux and macOS
$ which python
```

As long as your `virtualenv` is activated, pip will install packages into that specific environment and you'll be able to import and use packages in your Python application.

To leave your `virtualenv`, simply run:

```shell
$ deactivate
```

## Bonus: [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/)

To make working with virtual environments easier (especially for Windows uers), you can use `virtualenvwrapper`, which is a set of extensions to the `virtualenv` tool. It also places all of your virtual environments in a single location.

```shell
Mac:
$ pip install virtualenvwrapper
$ export WORKON_HOME=~/Envs
$ source /usr/local/bin/virtualenvwrapper.sh

Windows:
$ pip install virtualenvwrapper-win
```

Once you've installed `virtualenvwrapper`, create a new isolated development environment:

```shell
mkvirtualenv portfolio
```

This produced a folder named `portolio` inside the `Envs` folder with a clean copy of Python inside.

To activate `virtualenv` with `virtualenvwrapper`:

```shell
$ workon portfolio
```

You may also check the list of existing virtual environments in your `Envs` folder by typing:

```shell
$ workon
```

## Installing Flask

To install flask through `pip`, just run:

```shell
$ pip install flask
```

## Saving packages

To save the list of packages installed in your environment for easier reproduction:

```shell
$ pip freeze > requirements.txt
```

This will save what you've installed so far in a text file named `requirements.txt`.

To install the packages listed in a `requirements.txt` file:

```shell
$ pip install -r requirements.txt
```

### Getting crazy? Need help?
If you have questions, please feel free to ask and participate on our [Gitter group](https://gitter.im/WWCodeManila/Python).