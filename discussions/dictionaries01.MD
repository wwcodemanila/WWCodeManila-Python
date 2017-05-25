## Dictionaries

Imagine that we will create a simple PostalPH bot that allows a user to ask his/her postal code giving the bot his/her area.


```
PostalPHBot: Hello! What is your area?
Goblin: binondo
PostalPHBot: Hi! Your postal area is 1006.
```

How will you store the ff. mapping in Python?

```
Binondo: 1006
Intramuros: 1002
Malate: 1004
Ermita: 1000
Paco: 1007
Inagi-shi: 13225
Hino-shi: 13212
and many more...
```

Hmmm.... with a loooong conditional statements like this?

```python
area = input('Hello! What is your area?').lower()

if area == 'binondo':
    print('Hi! Your postal area is 1006.')
elif area == 'intramuros':
    print('Hi! Your postal area is 1004.')
# and a lot more if-else!

```

#### Creation and Value Access

Good thing, Python allows us to store collections for mapping or associating a `key` with a `value`, just like how a dictionary allows us to search for a word(the key) and its meaning(the value)!
Python dictionaries are collections just like lists but instead of having numbers as its index, we can use strings, numbers or tuples instead. Let's try to use dictionary to our postal bot!

```python
postal_mapping = {
    'binondo': 1006,
    'intramuros': 1002,
    'malate': 1004,
    'ermita': 1000,
    'paco': 1007,
    'inagi-shi': 13225,
    'hino-shi': 13212
}

area = input('Hello! What is your area?').lower()

if area in postal_mapping:
    print('Hi! Your postal area is {}'.format(postal_mapping[area]))
else:
    print('Sorry! The area you provided was not found on our records.')

```

We created a dictionary by enclosing in braces(`{}`) the key-value pairs which are separated by colon(`:`).

See how we accessed the dictionary value? We used strings(the area) as the dictionary key and used that `key` to retrieve the postal value.
```
your_dictionary[key]
```

Why did we check first if the area is in our dictionary? See what will happen if we have the code below and we input 'makati' to our postal bot.

```python
postal_mapping = {
    'binondo': 1006,
    'intramuros': 1002,
    'malate': 1004,
    'ermita': 1000,
    'paco': 1007,
    'inagi-shi': 13225,
    'hino-shi': 13212
}

area = input('Hello! What is your area?').lower()
# We removed the checking. YOLO!
print('Hi! Your postal area is {}'.format(postal_mapping[area]))
```

#### Dictionary update and methods

Postal Bot update! Let's add Quaipo to our dictionary and also, remove the odd Inagi-shi and Hino-shi as we found out it was for PostJP bot not PostPH bot!

```python
postal_mapping = {
    'binondo': 1006,
    'intramuros': 1002,
    'malate': 1004,
    'ermita': 1000,
    'paco': 1007,
    'inagi-shi': 13225,
    'hino-shi': 13212
}

# Let's add Quiapo
postal_mapping['quaipo'] = 1001

# Let's delete Inagi-shi
del postal_mapping['inagi-shi']

# Dictionaries have methods too!
# Let's delete Hino-shi using the pop method
deleted_value = postal_mapping.pop('hino-shi')
print('Removed {} from mapping'.format(deleted_value))

# Dictionaries have functions too!
# Let's print its length using the len function
print('We now have a total of {} postal mapping'.format(len(postal_mapping)))
```

### Challenge
Good job! You are nearly complete in knowing some basic programming concepts using Python! Let's get our fingers and mind working! 

Please see files under:
```
Gitlab project -> exercises -> dictionaries
```