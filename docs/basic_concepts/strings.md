## Definition
A string is a series of letters, numbers, symbols enclosed in single quote (‘) or double quote (“).

## Creation
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

## String methods
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

## Accessing string characters
Given a person's firstname and lastname, can we get the name initial?
![Name initials as avatar](https://i.stack.imgur.com/vBvgj.png)


!> Experiment on how to print the name initials with the code below!

```python
firstname = "Fred"
lastname = "Jowson"

# TRY TO FIGURE OUT HOW TO PRINT OUT THE NAME INITIALS
```

> We can access string characters through this syntax: **your_string[index]**

> Each character in a string is represented by an index number starting from 0

Here's an image to guide you with indexing.

![Python string indexing](https://developers.google.com/edu/python/images/hello.png)

Let's experiment more!

[my_strings](samples/my_strings.py ':include :type=code python')


## Immutable

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

!> Strings are **immutable**, meaning we cannot change it's value after creation.
Hence, the code above resulted to an error!


## Challenge
This summer, Aling Nena’s Sari-sari store wants to implement a reward system
where customers can redeem a reward by texting the following:

<**Reward number 1-9**> <**Customer’s name**> <**Gender f or m**>

```shell
>> Please enter text: 1 nicole i. tibay f
```

The system will then reply the following:

Hi <**Customer’s name Capitalized**>! You have successfully redeem
reward #<**reward number**> - <**reward**>! Thank you for choosing Aling Nena’s Sari-sari store.

```shell
>> Hi Nicole I. Tibay! You have successfully redeem reward #1 - Coke sakto!
Thank your for choosing Aling Nena’s Sari-sari store”
```

> Let’s assume that customers will always comply with the text format and give 1-9 number.

!> Please use below template

[filename](exercises/strings/strings01.py ':include :type=code python')

[challenge_partial](../challenge_partial.md ':include')


## Put your thinking cap on!

- What is the reasoning behind PEP8's break before binary operations?
- What does the `str()` function do?
- Do you find any difference in using `len(<your string>)` and `<your string>.lower()`? Can you explain?
- Explain string immutability.
