### Loops
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

##### For loop
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

##### While loop
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

#### Takeaways
* We can use `break`, `continue` and `pass` as control statements in the loop. Google it!
* `Infinite loop`: Use `while` loops with caution because if the expression did **NOT** resolve to a `False` the loooooooooooooop will go on forever just like below.

```python
is_hungry = True
while is_hungry:
    print('Vikings here I come!')

```
#### Challenge
During closing, Aling Nena counts from her vault the day's total income and
also the total amount of all her paper bills.

Help Aling Nena count her total income and total amount of her paper bills
from a list of cash money and using a loop!

Example:

```shell
>> Hi Aling Nena! Your total income for the day is 2947.
>> The total amount of your paper bills is 2920.
```

Just some notes:
* Please use and copy `loops01.py` as your template.

```shell
Git project -> exercises -> loops01 -> loops01.py
```

* Please rename the file as `<first name initial><middle name initial><last name>_loops01.py`. For example, John M. Doe will name his file as `jmdoe_loops01.py`.
* Share your work and contribute to the community! Please request membership to one of our GIT groups: [GitLab](https://gitlab.com/wwcodemanila) or [GitHub](https://github.com/wwcodemanila) 
* Please upload or push the file in our GIT repository (either in GitHub or GitLab) under the exercise folder.
* Present your work in front (#ApplaudHer)! You can also share your study group experience in social media and tag us!
 
## Further Challenge
* [Hackerrank](https://www.hackerrank.com/)
* [Checkio](https://checkio.org/)
* [Codefights](https://codefights.com/)
* [Codinggame](https://www.codingame.com/)