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
more [modular](https://www.quora.com/What-is-modular-programming-Where-is-it-used) and [reusable](https://www.quora.com/What-is-code-reusability)? Oh wait, can it also improve readability?

And we have `functions`!

## What is a function
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

## Writing our own function
To write your own function like below:

```python
# Declaration
def booster(number, boost=2):
    # Block of code (what the function does)
    print('Power booster!')
    # Return statement is optional
    return number * boost
```

1. **Declare** your function using the `def` keyword followed by your function name. 
2. Write the **arguments** enclosed in parenthesis followed by a colon `:`. Functions can accept arguments/parameters just like the `number` and `boost` in our booster function. We have two types of parameters:
  * **Required/Mandatory** - We need to provide the parameter value everytime we call the function just like `number`.
  * **Optional** - We can omit to pass the parameter and a default value will be given just like `boost`.
3. Write the task of the function (the block of code inside the function)
4. Write the return statement (Optional)

## Take aways
* [Playing with function parameters](http://pythoncentral.io/fun-with-python-function-parameters/)

## Challenge
Gooood job! You finished basic programming concepts with Python! For your last challenge...

Aling Nena's Sari-sari store just had a new neighbor! It's Mang Toto's ForEx!
Help Mang Toto to convert `USD, JPY, SGD` to `PHP` by:
* Asking the customer for their currency.

```shell
>> Welcome to Mang Toto's ForEx! What is your currency? We accept (usd, jpy, sgd):
```

* If they are not exchanging the currrency, notify the customer.

```shell
>> Welcome to Mang Toto's ForEx! What is your currency? We accept (usd, jpy, sgd): 
>> aud
>> Sorry! We do not exchange aud!
```

* If they are in their currency list, ask for the amount and inform the original and equivalent PHP amount.

```shell
>> Welcome to Mang Toto's ForEx! What is your currency? We accept (usd, jpy, sgd): 
>> usd
>> Your 100.50 usd is equivalent to 5069.22 PHP
```


!> Please use below template

[functions01](exercises/functions/functions01.py ':include :type=code python')

[challenge_partial](../challenge_partial.md ':include')


## Put your thinking cap on!

- What does `:.2f` do during string formatting?
- Should the required parameters be declared first on a function? Or we can order in YOLO the required and optional parameters?
- Are function parameters passed `by value` or `by reference`?
