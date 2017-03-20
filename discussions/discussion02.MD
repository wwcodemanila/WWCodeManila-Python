## Intro to PEP8

Scenario: Partner A told Partner B that the client wants to input the dividend amount
instead of hardcoding it. Partner A will be on Boracay for a month long
vacation and she left to you the source file.

```shell
Open our Gitlab project -> samples -> explain_me.py
```

As partner B, can you explain the code by just scanning it? Can you easily change
it to cater the new requirements?

Let's read [PEP8](https://www.python.org/dev/peps/pep-0008/) guidelines.

From PEP8:
* Readability counts - code is read much more often that it is written!
* The guideline is intended to improve the readability of code and make it consistent.
* It is not a guide not a law!

Now, try to rewrite the code and apply some PEP8 guides :)

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
print(f"{greeting} {rating} stars for them! {hashtag}")
# For compatibility with versions < Python3.6
# print("{} {} stars for them! {}".format(greeting, rating, hashtag))
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

Try running or typing the code under our samples folder, `my_strings.py`.

```python
# We can access string characters through this syntax:
your_string[<index>]
# Each character in a string is represented by an index number
# starting from 0
```

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

Strings are immutable, meaning we cannot change it's value after creation.
Hence, the code above resulted to an error!

## Challenge
This summer, Aling Nena’s Sari-sari store wants to implement a reward system
where customers can redeem a reward by texting the following:
`<Reward number> <Customer’s name> <Gender>

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
* Please use the template below to be able to print the reward,

```shell
Gitlab project -> exercises -> exercises02 -> exercises02.py
```

* Let’s assume for now that customers will always comply with the text format and give 1-9 number :)
* Enjoy!

## Slide Reference
Please view [here](https://docs.google.com/presentation/d/1iNpUAqxvEJwRDaSJRHw944pqy4MyZlYwwDiMPNmY1cU/edit?usp=sharing)




