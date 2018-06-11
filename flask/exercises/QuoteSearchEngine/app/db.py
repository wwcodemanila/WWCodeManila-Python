#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import sqlite3 as lite
import sys
 
con = lite.connect('quotes.db')
 
with con:
 
    cur = con.cursor()    
    # cur.execute("CREATE TABLE Quotes(Id INT, Value TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS Quotes(Id INT, Value TEXT)")

    quotes = ( "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
        "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
        "'To understand recursion you must first understand recursion..' -- Unknown",
        "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
        "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
        "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"  )

    for i, quote in enumerate(quotes):
        cur.execute("INSERT INTO Quotes VALUES(" + str(i) + ", " + repr(quote) + ")")