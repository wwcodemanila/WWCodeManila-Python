##  Goals

- [ ] Create and run your first Flask app
- [ ] Set the values of `FLASK_APP` and `FLASK_DEBUG` environment variables

## Getting Started

A minimal Flask application can easily be created in 3 steps and as little as **5 lines of code**.

1. Create a file named `app.py` inside your `portfolio` project folder:

```shell
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

2. In your terminal or console, navigate to the location of your project folder and set the `FLASK_APP` environment variable:

```shell
Mac:
export FLASK_APP=app.py

Windows:
set FLASK_APP=app.py
```

3. Finally, run your application:

```shell
flask run
```

Congratulations! You can now access your app through the url route generated in your terminal or console using your favorite browser.

To quit, press `CTRL+C`.

To deactivate your virtual environment, enter `deactivate`.

## Bonus: `FLASK_DEBUG` environment variable

To run your app in debug mode, set the `FLASK_DEBUG` environment variable to 1 before running the application:

```shell
Mac:
export FLASK_DEBUG=1

Windows:
set FLASK_DEBUG=1
```

### Getting crazy? Need help?
If you have questions, please feel free to ask and participate on our [Gitter group](https://gitter.im/WWCodeManila/Python).