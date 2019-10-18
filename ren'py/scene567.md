[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/WWCodeManila/Python)

At this point, we've covered all there is to discuss in our simple visual novel. 

We'll just need to complete our game with three more `label` blocks: reward, beach, ending.

Add these flags below where you defined the characters and before the `label start` block.

```python
define baonf = False
define beachf = False
define rewardf = False
```

Copy the assets `bg beach.png` and `nena sad.png` from the `assets` folder into `game/images`. 

# Scene 5

This scene is only run when both `$ correct_change` and `$ correct_item` are `True`.

Replace the `pass` statement in the `label reward` block in `script.rpy`:

```python
label reward:
    
    $ rewardf = True
    
    with fade
    show nena

    n "You did well, [name]! Because you helped me a lot today, I will give you a reward."
    n "Which will it be?"

    menu:
        "I can give you a baon to spend with your friends.":
            $ baonf = True
            u "Thanks for the allowance, Lola. I'll go play with Lita and Boy now."
            n "Go ahead, Apo. You deserve it."
            jump game
        "We'll go to the beach.":
            $ beachf = True
            u "Let's go the beach, Lola!"
            jump beach
```

Notice that in this scene, if the player decides to have a *baon* (allowance) as a reward, the game will run "back to" Scene 3 wherein we made a mini-game. `jump` statements can be powerful tools to facilitate any loops in the narration or storyline.

# Scene 6

Add the following in `script.rpy`:

```python
label beach:
    $ baonf = True
    scene bg beach with fade

    u "Wow, Lola! The beach is so pretty."
    n "Yes, it is. Glad you like it here."

    jump ending
```

# Scene 7 / Ending

Last, add the following in `script.rpy`, replace the statement under the `label ending` block:

```python
label ending:
    
    scene bg inside house with fade

    if rewardf:
        if baonf:
            "You were able to spend the rest of the day with your friends Lita and Boy."
            "You bought snacks for the three of you from the allowance Aling Nena gave you."
        elif beachf:
            pass

        "And just like that, your summer vacation in the province passed in bliss and happiness."

        with fade

        show nena

        u "Thank you Lola Nena for letting me stay with you for the summer."
        n "You're always welcome here, [name]."
        u "I'll comeback again next vacation!"
        n "Sure, apo!"

        scene bg inside house with fade

        "THE END"

    else:
        "You went home after a long day."
        show nena sad
        "Your Lola Nena is waiting for you. She doesn't look happy."
        n "Apo, I have called your Mom and Dad. They will fetch you here tomorrow."
        u "But.. but Lola..."

        if gamef:
            $ desc = "a lazy"
            n "You only played all day with your friends even though you promised to help me."
        elif storef:
            if correct_change == False:
                $ desc = "a dishonest"
                n "Bert told me that you did not give him the correct change."
                n "Instead, you pocketed the excess amount!"
            if correct_item == False:
                $ desc = "an untrustworthy"
                n "Tasya said that you didn't give her the correct reward."
                n "Instead, you kept it to your self!"
        
        n "I have no use for [desc] grandchild."

        scene bg inside house with fade

        "And just like that, your summer vacation in the province is OVER."

        "THE END"

    return
```

Try to run  the game using the Ren'Py launcher.

!> Tip: You can use  `Back` in the game screen to view the dialogue before or `Skip` to go ahead until some decision point is reached. Try these in order to view the different outcomes of your decision.

Note that in this scene, we have defined a variable by preceeding the variable name with `$ ` and equating it to a value, e.g.

```python
$ desc = "a lazy"
```

This is the same as when we previously defined a *flag* variable, although in this case we did not write a `define` statement for the `desc` variable first. You can do the same thing with our flag variables only that, sometimes, it is more readable to write or define the flags first thing in the code. (For instance, it's more efficient to find them after many lines of coding).

## Return statement

The `return` statement, like `label start` is another special statement in Ren'Py which means the end of the game. When this statement is run, no matter where in the game it is, the game immediately terminates.

For example, if we have inserted `return` in the `label beach` block before the `jump ending` statement:

```python
label beach:
    $ baonf = True
    scene bg beach with fade

    u "Wow, Lola! The beach is so pretty."
    n "Yes, it is. Glad you like it here."
    
    return
    jump ending
```

What do you think will happen? Try this by modifying this block as above. The game will immediately terminate without the character ever experiencing the ending! 

That's it! Congratulations on creating a simple virtual novel. 

# Project 

Make a visual novel of your own. Write or choose a story, gather your own assets, build awesome characters, make up interesting dialogues! Share your work! We'll love to play it! :heart:

[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/WWCodeManila/Python)

