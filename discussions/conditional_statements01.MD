## Conditional Statements
In our everyday living, we perform action based on a decision, situation or condition:
```shell
Take a taxi if we are already late for work; else, we will take the jeepney.
```

Now let's switch to our geeky world and alas, we were in a situation where:
* We only want to execute a block of code depending on a condition:
```shell
Add points to a customer if s/he presented a reward card.
```

* We need to perform different actions based on the situation:
```shell
Sends out SMS if customer has enough load, else prompt for an insufficient balance message.
```

Python offers decison making statements in order for us to conditionally execute a block of code. But before introducing those, let us recall that an action will only be executed if it meets a `condition` or `situation`, expressions that evaluates to `True` or `False`. Let's try to code some expressions!
```python
# Use literal values
is_late = True
is_card_presented = False
# Null or Zero values evaluates to False
customer_card = None
# Use operations
customer_load = 100
customer_load > 0
"Nissin".startswith("c")
```

Expressions? Checked! Let's dive to some Python decision making statements:
* If statements
```python
is_card_presented = False
customer_points = 10
if is_card_presented:
    # Can you shorten the expression below?
    customer_points = customer_points + 1
```

* If...else statements
```python
def send_message(message):
    # This is a function, we will learn more about this on our next session!
    print('Sending: {}'.format(message))

customer_load = 100
message = 'Happy to serve!'
if customer_load > 0:
    # call our function
    send_message(message)
    print('Your message is sent!')
    # Again, can you shorten the expression below?
    customer_load = customer_load - 1
else:
    print('You have insufficient balance.')
```

### Takeaways
* Notice how we group the actions(block of codes) above? We use the colon `:` to indicate the start of an indented block of code and grouped them by `whitespaces`.
* PEP8 recommends using `4` whitespaces for code indentation.

### Challenge
Please see files under:
```
Gitlab project -> exercises -> conditional_statements
```