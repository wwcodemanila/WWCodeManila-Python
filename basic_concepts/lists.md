So far, we have talked about some of the different data types in Python:

* integer
* float
* string
* boolean

 In the succeeding sections, we'll cover other commonly used data types in Python: list, tuples, sets, and dictionaries. 

## List

A list stores a collection of elements in Python. Actually, it may not contain any element at all. A list starts and ends with square brackets `[` and `]` and uses commas `,` to separate each element. These elements could be of the same, or different data types.

### Creating lists

To create a list, simply put comma-separated elements inside square brackets, as shown below:

```python
# a list containing the same data types (strings)
a = ["hey", "there", "you"]

# list of mixed data types
b = [1, 2, "papaya"]

# list of lists
c = [[1,2], [3, 4]]

# list of dictionaries (dictionaries will be covered in the succeeding section)
d = [{"a": "apple"}, {"b": "ball"}]
```

You can also create an empty list just by typing two square brackets: 

```python
x = [ ]
```

Or using the `list()` function

```python
e = list() 
print(e)
```

You can use the same function to convert strings into list

```python
w = "womenwhocode"
w_list = list(w)
print(w_list)
```

!> Try `list()` on other data types.

Lists can be created from other lists by slicing (see below).


### Accessing and slicing lists 

Accessing elements in a list is the same as accessing elements in strings: you use integer indices

```python
colors = ["red", "blue", "green"]
print(colors[0])
print(colors[2])
print(colors[-2])
```

```shell
red
green
blue
```

Slicing elements involves specifying a range of indices using `:`. 

```python
rhyme = [1,2,"buckle","my", "shoe", 3, 4]
words = rhyme[2:-2]
print(words)
```

Notice that slicing a list produces a list as well.

```python
print(type(words))
```

```
<class 'list'>
```

### Updating lists

Once created, a list can be changed. That is, we consider them **mutable** objects in Python. Thus, one way to update a list is to re-assign a value to a particular index or indices.

```python
odd = [2, 4, 6, 8] # not odd at all

odd[0] = 1 # change the first value
print(odd)

odd[1:] = [3, 5, 7] # change the rest of the values
print(odd)

```

```
[1, 4, 6, 8]
[1, 3, 5, 7]
```

Elements can also be added to lists

```python
odd.append(9) # add to a number to end of list
print(odd)

odd.extend([11, 15]) # append the contents of a sequence ([11, 15]) to list
print(odd)

odd.insert(-1, 13) # insert object (13) at position (-1)
print(odd)
```

```
[1, 3, 5, 7, 9]
[1, 3, 5, 7, 9, 11, 15]
[1, 3, 5, 7, 9, 11, 13, 15]
```

!> Notice that applying these methods changes the list itself. Think of ways in which this could be useful. Think of where this may not be ideal for your code or application.

Deleting elements in a list can be done in several ways:

```python
my_list = ["p", "r", "o", "b", "l", "e", "m"]

del my_list[2]          # remove the element in my_list[2]
print(my_list)

my_list.remove("p")     # remove the first occurence of "p"
print(my_list)

my_list[2:3] = []       # substitute element in [2:3] thereby removing them
print(my_list)          #   from list. 

my_list.pop()           # remove the last element
print(my_list)

my_list.pop(1)          # remove the element in index 1
print(my_list)

my_list.clear()         # remove all elements
print(my_list)
```

```
['p', 'r', 'b', 'l', 'e', 'm']
['r', 'b', 'l', 'e', 'm']
['r', 'b', 'e', 'm']
['r', 'b', 'e']
['r', 'e']
[]
```

!> Note that, out of the above methods, only `pop` returns a value. What happens when we use a single index instead of range in the second example above? i.e. `my_list[2] = []`

An entire list can also be deleted using the `del` statement. Printing the list results in an error, confirming that the list has been deleted.

```python
del my_list
print(my_list)
```
```
Traceback (most recent call last):
  File "test.py", line 21, in <module>
    print(my_list)
NameError: name 'my_list' is not defined
```


### Basic operations

Like strings, the operations `*` and `+` can be applied to lists. The results of these are new lists.

```python
x = ["a", "b", "c"] + [1, 2, 3]
y = ["hello"] * 3
z = 3 * ["world"]

print(x)
print(y)
print(z)
```
```
['a', 'b', 'c', 1, 2, 3]
['hello', 'hello', 'hello']
['world', 'world', 'world']
```

!> Remember that `+` is permissible only on two or more *lists* while `*` is permissible between a *list* and an *integer*. 


Here are other functions and methods that can be applied to a list (e.g. `list`). Try them for your self to see what they can do:

- `len()`
- `max()`
- `min()`
- `list.count()`
- `list.index()`
- `list.reverse()`
- `list.sort()`


## Tuple

Tuples are similar to lists in that they contain zero or more comma-separated elements of the same or different data types. However, one important thing to remember about tuples is that they are **immutable**; that is, unlike lists (and similar to strings) once a tuple is created, it cannot be changed. 

Tuples are bounded by parentheses `(` and `)`:

```python
tup1 = ("t", )                  # tuple with one element
tup2 = ("hello", "world")       # tuple containing the same data type i.e. strings
tup3 = (1, "a", 1.5)            # tuple containing different data types
tup_e = ()                      # an empty tuple
tup4 = ([1, 2, 3], "4")        # a tuple containing a list
tup5 = (("x", "y", "z"), (1, 2, 3))    # a tuple containing tuples
```

!> Notice that there is a trailing comma when we defined the tuple `tup1 = ("t", )` containing a single element. Why do you think is this necessary? What happens if we leave out the comma at the end? 


Accessing and slicing elements in a tuple also makes use of integer indices and ranges of indices `:`:

```python
print(tup2[1])
print(tup3[0:2])
```

```
'world'
(1, 'a')
```

!> Try slicing a tuple and check the data type of the result.

Similar to list, a tuple can be created from a string using the function `tuple()`:

```python
t = tuple("code")

print(t)
```

You can convert a list to a tuple using `list()`, and convert a tuple to a list using `list()`

```python
m = tuple(["make", "me", "a", "tuple"])
n = list(("make", "me", "a", "list"))

print(m)
print(n)
```

```
('make', 'me', 'a', 'tuple')
['make', 'me', 'a', 'list']
```


### Updating tuples

Consider the following: 

```python
x = (1, 2, 4)

x[-1] = 3
```

What happens when we tried to substitute a value? 

Since tuples are immutable, updating and deleting a value within a tuple is not possible and will result in an error. We can, however, think of another way to come up with the desired elements. In the example above, we want a tuple with three consecutive numbers `(1, 2, 3)`. While updating an immutable object is not possible, we can define new tuples instead and perform a combination of operations.

```python
z = x[0:-1]
y = (3, )

t_cons = z + y

print(t_cons)
```

```
(1, 2, 3)
```

An entire tuple can be deleted using the `del` statement. Printing the tuple after it has been deleted results in an error (`NameError`), confirming that the deletion has taken place.

```python
del t_cons

print(t_cons)
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 't_cons' is not defined
```

### Basic operations

As illustrated in a previous example, `+` is permitted on tuples. Likewise, `*` can be used, resulting in new tuples.

```
a = ("hi",) + ("hello",)
b = ("bye",) * 3

print(a)
print(b)
```

```
('hi', 'hello')
('bye', 'bye', 'bye')
```

A similar logic applies to tuples as list when using these operations: `+` can be applied to two or more *tuples*, `*` works with a *tuple* and an *integer*.

Here are other functions that work with tuples. Try the following and see what they can do:

- `len()`
- `max()`
- `min()`

## Set

A set is an *unordered* collection of data that has *no duplicate elements*. A set in Python is what it sounds like from your math lessons: it can be used to carry out operations like union, intersection, and differences. 

We will not dwell too much on sets during this study group, but in case you might have a use for sets and set operations in the future, you can read more about these [here](https://www.programiz.com/python-programming/set).

A set consists of zero or more comma-separated elements within curly braces `{` and `}`. The values may or may not be of the same data types. Likewise, the `set()` function can be used to make an empty set, or convert a list or tuple to a set. 

The following are examples of sets

```python
set1 = {1, 2, 3}
set2 = {("a", "b",), 3.0}
```

!> Simply using `{}` does not result in a set (e.g. `e = {}`). What would the type be?

The following will result in an error

```python
x = {[1, 2, 3], 4}
y = {{1, 2, 3 }, 4}
```
This is because both lists and sets can change over time (they are mutable ~ unhashable), unlike tuples and strings which are immutable and therefore permitted in sets. Dictionaries, discussed in the succeeding section, are also mutable and therefore cannot be contained in sets.

As mentioned, sets are *unordered*, hence accessing an element using integers and slicing using a range of indices do not make sense in a set and will therefore result in an error.


```python
set1[0]
```

Also the elements in sets are *deduplicated*. Even though you intentionally wrote a set with duplicate elements, these will still be stored as a single entities.

```python
set3 = {1,1,1,1}
print(set3)
```


### Updating a set

While indices have no meaning in sets, sets are still mutable. Hence, elements in a set can be updated and/or removed.

```python
my_set = {1, 3, 6}
print(my_set)

my_set.add(2)
print(my_set)

my_set.update([4, 5])
print(my_set)

my_set.update([6,7], {8,9})
print(my_set)
```

```
{1, 3, 6}
{1, 2, 3, 6}
{1, 2, 3, 4, 5, 6}
{1, 2, 3, 4, 5, 6, 7, 8, 9}
```

To remove elements or the set itself:

```python

another_set = {1, 2, 3, "a", "b", "c"}
print(another_set)

another_set.discard(3)          # discard 3
print(another_set)

another_set.remove(2)           # remove 2
print(another_set)

another_set.discard(3)          # discard 3 again
print(another_set)

another_set.remove(3)           # remove 3

another_set.clear()             # remove all elements in set
print(another_set)

del another_set                 # delete the set itself
print(another_set)
```

!> From running the code above, what do you think is the difference between `.remove()` and `.discard()`?


## Challenge


!> Please use the template below

[filename](exercises/lists/list.py ':include :type=code python')

[challenge_partial](../challenge_partial.md ':include')


## Put your thinking cap on!

- How is an **array** in Python different from a list?
- We've briefly covered **mutable** (e.g. list, sets) and **immutable** (e.g. strings) objects in Python. What other objects are considered mutable? How about immutable?
- Strings, lists, and tuples have plenty in common in terms of the methods and operations that can be done to them. Why do you think this is so?

