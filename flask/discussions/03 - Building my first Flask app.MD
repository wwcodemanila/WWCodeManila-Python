A minimal Flask application can easily be created in 3 steps and as little as *5 lines of code*.

1. Create a file named `hello.py` inside your `HelloWorld` project folder (~/Envs):

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
export FLASK_APP=hello.py

Windows:
set FLASK_APP=hello.py
```

3. Finally, run your application:

```shell
flask run
```

Congratulations! You can now access your app through the url route generated in your terminal or console using your favorite browser.

To quit, press `CTRL+C`.

To deactivate your virtual environment, enter `deactivate`.

### Getting crazy? Need help?
If you have questions, please feel free to ask and participate on our [Gitter group](https://gitter.im/WWCodeManila/Python).