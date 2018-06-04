from flask import Flask, render_template
from random import randint
app = Flask(__name__)
 
@app.route("/")
def index():
    return "Welcome!"
 
@app.route("/members/")
def members():
    return "Members"
 
@app.route("/members/<string:name>/")
def getMember(name):
    quotes = [ "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
        "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
        "'To understand recursion you must first understand recursion..' -- Unknown",
        "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
        "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
        "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"
    ]
    randomNumber = randint(0,len(quotes)-1) 
    quote = quotes[randomNumber]

    return render_template('test.html',**locals())
 
if __name__ == "__main__":
    app.run()