from flask import Flask, render_template # Import render_template.
from random import randint #Import randint.
app = Flask(__name__)

@app.route("/")
@app.route("/home/")
def home():
	return "Home"

@app.route("/about/")
def about():
	# Syntax: render_template(filename)
	return render_template("about.html")

@app.route("/skills/", defaults={'username': None})
@app.route("/skills/<string:username>/")
def skills(username):
	# Syntax: render_template(filename, variable/s)
	return render_template("skills.html", username=username)

@app.route("/projects/")
def projects():
	projects = ["Facebook", "Twitter", "Instagram", "Uber", "Grab"]
	# Use randint() to generate a random integer.
	# Syntax: randint(lowest number, highest number)
	randNo = randint(0, len(projects) - 1)
	project = projects[randNo]

	# Use **locals() to pass multiple variables.
	return render_template("projects.html", **locals())

@app.route("/contact/")
def contact():
	return "Contact"