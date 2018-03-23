## Intro to PEP8

`Scenario:` Partner A told Partner B that the client wants to input the dividend amount
instead of hardcoding it. Partner A will be on Boracay for a month long
vacation and she left to you the source file, [explain_me.py](https://github.com/wwcodemanila/WWCodeManila-Python/blob/master/samples/explain_me.py).

```shell
Open our Gitlab project -> samples -> explain_me.py
```

As partner B, can you explain the code by just scanning it? Can you easily change
it to cater the new requirements?

Let's read [PEP8](https://www.python.org/dev/peps/pep-0008/) guidelines.

From PEP8:
* Readability counts - code is read much more often that it is written!
* The guideline is intended to improve the readability of code and make it consistent.
* It is a guide not a law!

Now, which of the ff. are PEP8 compliant?

``` python
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)
```

or

```python
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

```

## String pa more
A string is a series of letters, numbers, symbols enclosed in single quote (‘) or double quote (“).

### String creation
Let's try some ways to create strings!

```python
greeting = "WWC is awesome!"
title = 'StringPaMore'
hash_symbol = "#"
hashtag = hash_symbol + title
rating = str(5)
print("{} {} stars for them! {}".format(greeting, rating, hashtag))
# print(f"{greeting} {rating} stars for them! {hashtag}")  # For versions Python3.6
```

### String methods
Let's try some string methods!

```python
movie_title = "My ex and whys"
print(len(movie_title))

comment = "HINDI AKO GALIT!"
print(comment.lower())
print(comment.islower())

shout = "darna!"
print(shout.upper())
```

### Accessing string characters
Given a person's firstname and lastname, can we get the name initial?
![Name initials as avatar](https://i.stack.imgur.com/vBvgj.png)

```python
firstname = "Fred"
lastname = "Jowson"
# Can you try print out the name initials?
```

Try running or typing the code under our samples folder, [my_strings.py](https://github.com/wwcodemanila/WWCodeManila-Python/blob/master/samples/my_strings.py).

```python
# We can access string characters through this syntax:
your_string[<index>]
# Each character in a string is represented by an index number
# starting from 0
```

Here's an image to guide you with indexing.
![Python string indexing](https://developers.google.com/edu/python/images/hello.png)

Now, since we can access characters from a string, let's try to change its value!
Is the code below successful?

```python
mispelled_word = "beleive"
# This should raise an error
mispelled_word[3] = "i"
mispelled_word[4] = "e"

# What we can do is to re-assign the variable to a new string
mispelled_word = "believe"
```

Strings are **immutable**, meaning we cannot change it's value after creation.
Hence, the code above resulted to an error!

## Challenge
This summer, Aling Nena’s Sari-sari store wants to implement a reward system
where customers can redeem a reward by texting the following:
`<Reward number 1-9> <Customer’s name> <Gender f or m>`

```shell
>> Please enter text: 1 nicole i. tibay f
```

The system will then reply the following:
`Hi <Customer’s name first letters upper case>! You have successfully redeem
reward #<reward number> - <reward>! Thank you for choosing Aling Nena’s Sari-sari store.`

```shell
>> Hi Nicole I. Tibay! You have successfully redeem reward #1 - Coke sakto!
Thank your for choosing Aling Nena’s Sari-sari store”
```

Just some notes:
* Please use this [template](https://github.com/wwcodemanila/WWCodeManila-Python/blob/master/exercises/exercises02/exercises02.py) to be able to print the reward.

```shell
Gitlab project -> exercises -> exercises02 -> exercises02.py
```

* Let’s assume for now that customers will always comply with the text format andgive 1-9 number :)
* Please rename the file as `<first name initial><middle name initial><last name>_execise02.py`. For example, John M. Doe will name his file as `jmdoe_exercise02.py`.
* Share your work and contribute to the community! Complete how-to share your work instruction [here](https://github.com/wwcodemanila/WWCodeManila-Python/blob/master/exercise_upload_step.md).
  * Create a Github account if none yet and create a repository for wwcode-python. You will upload your works there.
  * Please upload or push the file in your GIT repository.
  * Open an issue in our repository named `<Your name> - <topic>`. For example, `John Doe - Loops`.
  * Share the link of your work on the issue.
* Present your work in front (#ApplaudHer)! You can also share your study group experience in social media and tag us!
* Enjoy!



## Put your thinking cap on!

- What is the reasoning behind PEP8's break before binary operations?
- What does the `str()` function do?
- Do you find any difference in using `len(<your string>)` and `<your string>.lower()`? Can you explain?
- Explain string immutability.


## Getting crazy? Need help?
If you have questions, please feel free to ask and participate on our [Gitter group](https://gitter.im/WWCodeManila/Python).


## Further Challenge
* [Hackerrank](https://www.hackerrank.com/)
* [Checkio](https://checkio.org/)
* [Codefights](https://codefights.com/)
* [Codinggame](https://www.codingame.com/)
