[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/WWCodeManila/Python)

# Scene 2

Our next scene happens on your way to Aling Nena's store. You bump into your friends Lita and Boy and you're now faced with another decision - will you break your promise to Aling Nena or remain true to your words?

In implementing this scene, we'll learn about:

- [ ] Positioning images
- [ ] Transitions
- [ ] Flags and if-else statements
- [ ] Jump statements

You'll first need to add two characters before the `label start` block along with the previous two characters. 

```python
define b = Character("Boy")
define l = Character("Lita")
```

In addition, we'll define two other variables called `gamef` and `storef` and set their values to `False`. Write them just below where you defined the characters before the `label start` block.

```python
define gamef = False
define storef = False
```

Next, copy the assets `bg street.png` ,  `lita.png`, and `boy.png` from the `assets` folder into `game/images`. 

Here is the full code for the next scene. Copy the following code into `script.rpy` after the `label start` block. It's a new `label` statement so it should not be indented inside the previous block.

```python
label street:

    scene bg street with fade

    show nena

    n "Right, let's get started. We need to go to my Sari-sari store. Please help me for the day, Apo."
    
    hide nena
    
    show lita at left with moveinright
    l "Hi, Aling Nena and [name]!"

    show boy at right with moveinleft
    b "Hello po!"
    b "Long time no see, [name]! Tara, let's play!"

    show nena
    n "Naku apo, you said you'll help me."

    menu:
        "Lola, mamaya na. I'll play with my friends first.":
            n "Ay naku, apo. Bahala ka."
            jump game
        "Sorry Lita and Boy, I promised my Lola I'll help her today.":
            jump store
            
label store:
    $ storef = True
    pass
```

Create a new script called `batobato.rpy`. Write the following code:

```python
label game:
    $ gamef = True
    pass
```

Try to run  the game using the Ren'Py launcher.

!> Tip: You can use  `Back` in the game screen to view the dialogue before or `Skip` to go ahead until some decision point is reached. Try these in order to view the different outcomes of your decision.

## Positioning images

Continuing with our discussion about inserting images to our visual novel, positioning images in Ren'Py is as straight forward as using the `at` preposition, e.g:

```python
show lita at left
```

Ren'Py has a pre-defined set of positions: `left`, `right`, `center` (default), and `truecenter` (centered horizontally and vertically). You can also define your own custom position using the `Position()` class. We'll revisit how to use this class later in Scene 4.  

## Transitions

Instead of simply popping in a scene or character image, transitions can be used to aide your storytelling. Like positions, this can simply be introduced using `with`:

```python
scene bg street with fade
```

Transitions can be combined with positions:

```python
show lita at left
with moveinright
```

which is the same as 

```python
show lita at left with moveinright
```

Like positions, Ren'Py has predefined transitions such as `fade`, `dissolve`, and `pixellate`. Likewise, you can define your own transitions using the different *transition classes*. You can learn more about the different pre-defined transitions and transition classes [here](https://www.renpy.org/doc/html/transitions.html).

## Jump statement

The `jump` statement indicates that a particular `label` statement should be run next:

```python
#...
    menu:
        "Play":
            # ... 
            jump game
        "Store":
			# ...
            jump store
label game:
    "Player chooses play"
label store:
    pass
```

You can think of the label name as pointers and the jump names as directives to run codes in these pointers next.

If you haven't decided what to put inside the next `label` block yet, you can prepare a `label` statement beforehand and just use`pass`, just like a regular Python `pass` statement:

```python
label store:
    pass
```

 Otherwise, the game will terminate in an error when it couldn't find the the next labelled block. 

Let's fill out `label game` and `label store` in Scenes 3 and 4.

## Flags and If-else statements

In our game, it is important to remember the choices of the player since some of these choices can determine what happens  later on.

Ren'Py supports the use of *flags*.  Just like characters, these can be set using the `define` statement before the `label` block. 

```python
define flag = False
label game:
    $ flag = True
label home:
    "Home"
```

Later on in the game, these flags can be used in an `if-else` statement. 

```python
label evaluate:
    if flag:
        "You played a game."
    else:
        "You went home."
```

Notice that you don't have to define an `if-else` statement inside a `python` block and that instead of writing the variable as `$ flag` in the `if` statement, you just use the name of the variable without `$`. If you need this variable outside the `if-else` or even `elif` statements, you'll need to precede it as `$ flag`. 

In our code above for Scene 2, the variables `gamef` and `storef` are first set to `False` and then switched to `True` when the game ran the respective `label` blocks ... which, in turn, depended on the choice of the player under the `menu` block:

```python
define gamef = False
define storef = False

# ...

label street:

# ...

    menu:
        "Lola, mamaya na. I'll play with my friends first.":
            n "Ay naku, apo. Bahala ka."
            jump game
        "Sorry Lita and Boy, I promised my Lola I'll help her today.":
            jump store
            
label store:
    $ storef = True
    pass
```

and in `batobato.rpy`

```python
label game:
    $ gamef = True
    pass
```

This is how the game remembers that a particular choice has been made. It doesn't really matter if you change the value of the flag inside the `menu` block or inside the `label` block, so long as this aides the readability of your code i.e. if you write all other flags in your code in the same manner.

We'll use this values later on in the `label ending` block, in Scene 7 (the last scene):

```python
label ending:
    #...
    	if gamef:
        #...
        elif storef:
		# ..
```



In the next part, we'll learn how to use other Python equivalent statements in Ren'Py by making a mini-game *bato-bato pik* (rock, paper, scissors).

[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/WWCodeManila/Python)

