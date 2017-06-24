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


    def send_message(message):
        # This is a function, we will learn more about this on our next session!
        print('Sending: {}'.format(message))
```

### Takeaways
* Notice how we group the actions(block of codes) above? We use the colon `:` to indicate the start of an indented block of code and grouped them by `whitespaces`.
* PEP8 recommends using `4` whitespaces for code indentation.

### Challenge
Aling Nena stores her soft drink stock on two refrigerators.
She stores `Coke, Sprite and Royal` on her Sari-sari store's refrigerator while
`RC and 7UP` can be found on her house's refrigerator.

Help Aling Nena to properly respond to her customer when buying softdrinks.

The reply will depend if the soft drink brand is on the store's ref,
on the house's ref or none. If the customer buys a soft drink brand that is:
1. stored on the store, she will respond `Got it!`
2. stored on the house, she will respond `Please wait for a while!`
3. not sold by her, she will respond `Sorry we do not sell that. We only have <input here the soft drink brands>`
    

Just some notes:
* Please see use and copy the file as your template:

```
Gitlab project -> exercises -> conditional_statements
```

* Please rename the file as `<first name initial><middle name initial><last name>_conditional01.py`. For example, John M. Doe will name his file as `jmdoe_conditional01.py`.
* Share your work and contribute to the community!
  * Create a Github account if none yet and create a repository for wwcode-python. You will upload your works there.
  * Please upload or push the file in your GIT repository.
  * Open an issue in our repository named `<Your name> - <topic>`. For example, `John Doe - Loops`.
  * Share the link of your work on the issue.
* Present your work in front (#ApplaudHer)! You can also share your study group experience in social media and tag us!
* Enjoy!

## Further Challenge
* [Hackerrank](https://www.hackerrank.com/)
* [Checkio](https://checkio.org/)
* [Codefights](https://codefights.com/)
* [Codinggame](https://www.codingame.com/)