##  Goal

- [ ] Understand the different types of URL routes

## Getting Started

Open `app.py` from the portfolio project that you created last time.

1. Replace the `hello_world` function name to `home` and change the return string from `Hello, World!` to `Home`.

```shell
@app.route("/")
def home():
	return "Home"
```

The text `Home` should now be displayed when you run your application.

2. Add `@app.route("/home/")` after `@app.route("/")`.

```shell
@app.route("/")
@app.route("/home/")
def home():
	return "Home"
```

You should now be able to see the same display text when you go to `<URL>/home/` (e.g. http://127.0.0.1:5000/home/).

3. Copy and paste the next function `about` to your code.

```shell
@app.route("/about")
def about():
	return "About"
```

If you try to access `<URL>/about`, you should be able to see the text `About`. However, if you try to access `<URL>/about/`, you will encounter a 404 encounter.

To fix this, add a trailing slash (/) after the route name. This would let you access the URL regardless of whether you have a trailing slash or not.

4. Create a subroute of `about` that will allow users to input their location in the URL.

```shell
@app.route("/about/<location>/")
def about_location(location):
	return "I am from %s." % location
```

If you try to access `<URL>/about/Earth/`, the text `I am from Earth.` will be displayed.

5. Add another route for `skills`.

```shell
@app.route("/skills/")
def skills():
	return "Skills"
```

Then add a subroute that would accept the user's `toeic_score` as an integer.

```shell
@app.route("/skills/<int:toeic_score>/")
def skills_toeic(toeic_score):
	return "My TOEIC score is %d / 90." % toeic_score
```

This allows you to specify the data type of the input that you'll receive.

6. Add a route named `projects` which accepts an integer named `amount`. Set the default value of `amount` to `0`.

```shell
@app.route("/projects/", defaults={'amount': 0})
@app.route("/projects/<int:amount>")
def projects(amount):
	return "I have %d project/s to date." % amount
```

This allows you to avoid displaying an invalid page in case there's no input from the user.

7. Lastly, add a route named `contacts`.

```shell
@app.route("/contact/")
def contact():
	return "Contact"
```

## Congratulations!

Your portfolio now contains 5 main pages:

* Home
* About
* Skills
* Projects
* Contact

Feel free to customize them and their contents!
