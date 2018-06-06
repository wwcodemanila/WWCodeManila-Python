Can you tell what the code below does?
```python
continents = ['Africa', 'Antarctica', 'Asia', 'Australia/Oceania', 'Europe', 'North America', 'South America']
print(continents[0])
print(continents[1])
print(continents[2])
print(continents[3])
print(continents[4])
print(continents[5])
print(continents[6])
```

Yes! It prints out the continents of the world! You may have noticed that this is a situation where we want to do some action on each item in a list (in this case, that is to print out the continent name). But what if we have a list containing all the countries of the world and wanted to print out each country? Do we need to painstakingly write a hundred of print statements? Or you started thinking, `Is there a way that allows us to go through the list and execute the same action multiple times`?

Yes! Python loops allows us to:
* Iterate through the list and perform an action to each element of the list
* Execute a block of code multiple times

## Syntax

### For loop
The `for` loop has the ff. syntax:
```shell
for <item> in <list>:
    <the block of actions to be executed for each item>
```

Say no to repeated lines of code! Let's rewrite the code above using a for loop!
```python
continents = ['Africa', 'Antarctica', 'Asia', 'Australia/Oceania', 'Europe', 'North America', 'South America']
for continent in continents:
    print(continent)

# Will print out
# Africa
# Antarctica
# Asia
# Australia/Oceania
# Europe
# North America
# South America
```

### While loop
The `while` loop has the ff. syntax:
```shell
while <expression>:
    <statement/s>
```

The `while` loop allows us to repeatedly execute a block of code as long as the expression evaluates to `True`. Let's do a New Year countdown!
```python
count = 10
while count > 0:
   print(count)
   count = count - 1
print('Happy New Year!')
```

## Takeaways
* We can use `break`, `continue` and `pass` as control statements in the loop. Google it!

!> Beware of Infinite loop! Use `while` loops with caution because if the expression did **NOT** resolve to a `False` the loooooooooooooop will go on forever just like below.

```python
is_hungry = True
while is_hungry:
    print('Vikings here I come!')

```


## Challenge
During closing, Aling Nena counts from her vault the day's total income and
also the total amount of all her paper bills.

Help Aling Nena count her total income and total amount of her paper bills
from a list of cash money and using a loop!

Example:

```shell
>> Hi Aling Nena! Your total income for the day is 2947.
>> The total amount of your paper bills is 2920.
```


!> Please use below template

```python
""" Aling Nena's Cashier Challenge
Author:
Description: During closing, Aling Nena counts from her vault the day's total income and
also the total amount of all her paper bills.

Help Aling Nena count her total income and total amount of her paper bills
from a list of cash money and using a loop!
"""


def is_coins(money):
    """ Determine if the money is a coin
    :param money: (Integer)
    :return: (Boolean)

    Examples:
        >>>  print(is_coins(20))
        False
        >>>  print(is_coins(1))
        True
    """
    if money < 20:
        return True
    return False


cash_on_vault = [1, 5, 100, 10, 50, 50, 20, 5, 1, 1000, 1000, 500, 5, 200]

# Build your code below

```

> Share your work and contribute to the community! Complete how-to share your work instruction [here](getting_started/exercise_upload_step.md).

> Present your work in front (#ApplaudHer)! You can also share your study group experience in social media and tag us!

> Enjoy!

## Put your thinking cap on!

- What are the specific characteristics of the `for` and `while` loop?
- What is the effect of `break`, `continue` and `pass` control statements in a loop?
