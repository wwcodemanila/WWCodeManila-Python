## Functions

Let's have a simple USD-PHP converter program!
```python
exchange_rate = {'usd': 50.44, 'jpy': 0.45} 
dollars = float(input("How much USD?"))
peso = dollars * exchange_rate['usd']
print("Hello! your {}USD is equivalent to {:.2f}PHP".format(dollars, peso))
```

But what if we also want make use of the JPY-PHP conversion? Maybe we can tweak some code above?
```python
exchange_rate = {'usd': 50.44, 'jpy': 0.45} 
dollars = float(input("How much USD?"))
peso = dollars * exchange_rate['usd']
print("Hello! your {}USD is equivalent to {:.2f}PHP".format(dollars, peso))

jpy = float(input("How much JPY?"))
peso = jpy * exchange_rate['jpy']
print("Hello! your {}JPY is equivalent to {:.2f}PHP".format(jpy, peso))
```

Can you look again and check if there are lines of code that does the same thing? What if we can reuse those to make our code
more [modular](https://www.quora.com/What-is-modular-programming-Where-is-it-used) and [reusable](https://www.quora.com/What-is-code-reusability)?

And we have `functions`!

#### What is a function
We have encountered functions before! Specifically, [builtin functions](https://docs.python.org/3/library/functions.html) which are functions provided by Python packages and libraries.
Remember this?

```python
str = "Banana"
# len and print are actually functions!
print(len(str))
```

From here can you try to explain to yourself what functions are? `Functions` are just a block of reusable code that does some tasks!
The `len` function accepts an object and returns it length! Now we can reuse that function anywhere in our code to get
the length of objects like strings or dictionaries!
