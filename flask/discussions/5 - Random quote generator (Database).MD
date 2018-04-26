# Random Quote Generator meets Database

Let's update our random quote generator to retrieve quotes from a SQLite database!

## First step: Create your database

Create and run your `db.py` file.

```python
import sqlite3 as lite
 
con = lite.connect('quotes.db')
 
with con:
 
    cur = con.cursor()    
    cur.execute("CREATE TABLE IF NOT EXISTS Quotes(Id INT, Value TEXT)")

    quotes = ( "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
        "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
        "'To understand recursion you must first understand recursion..' -- Unknown",
        "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
        "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
        "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"  )

    for i, quote in enumerate(quotes):
        cur.execute("INSERT INTO Quotes VALUES(" + str(i) + ", " + repr(quote) + ")")
```

Check if your `quotes.db` database was created.

## Second step: Get quote from database

We need to update your `hello` function to get the quote from the created database.

```python
@app.route("/members/<string:name>/")
def hello(name):
    # UPDATE NEEDED: Connect to your database
    con = None 

    with con:
        # UPDATE NEDED: Get all quotes
        cur = None
        cur.execute("")

        quotes = None
    
    randomNumber = randint(0,len(quotes)-1)
    quote = quotes[randomNumber][1]
    
    return render_template('hello.html', **locals())
```

Run your application!


### Challenge

Create a search route `/search/<string:search>/` that will return all 
quotes from the database containing the search string!

[Search template](https://github.com/wwcodemanila/WWCodeManila-Python/tree/master/flask/assets/search.html) 


```python
@app.route("/search/<string:search>/")
def search(search):
    results = []

    con = None

    with con:
        cur = None
        cur.execute("")

        quotes = None

    # Filter quotes that contains a substring of your search term
    
    return render_template('search.html',**locals())
```

### Getting crazy? Need help?
If you have questions, please feel free to ask and participate on our [Gitter group](https://gitter.im/WWCodeManila/Python).

### References

*  [SQLite Installation](https://www.tutorialspoint.com/sqlite/sqlite_installation.htm)
*  [Python + Sqlite](https://pythonspot.com/en/python-database-programming-sqlite-tutorial/)
*  [Slides](https://docs.google.com/presentation/d/1yzyAuDip0rmlrZ_MD3aU1ryXStHzcInKldD0gKYDkmY/edit?usp=sharing)
