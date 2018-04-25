#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from random import randint
app = Flask(__name__)

import sqlite3 as lite
import sys
 
@app.route("/")
def index():
    return "Welcome!"
 
@app.route("/members/")
def members():
    return "Members"
 
@app.route("/members/<string:name>/")
def getMember(name):
    con = lite.connect('app\quotes.db')

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Quotes;")

        quotes = cur.fetchall()
    
    randomNumber = randint(0,len(quotes)-1)
    quote = quotes[randomNumber][1]
    return render_template('test.html',**locals())

@app.route("/search/<string:search>/")
def search(search):
    results = [];

    con = lite.connect('C:\\Users\\aalvara2\\Envs\\QuoteGenerator\\app\\quotes.db')

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Quotes;")

        quotes = cur.fetchall()

    for quote in quotes:
        if search.upper() in quote[1].upper():
            results.append(quote[1])
    
    return render_template('search.html',**locals())