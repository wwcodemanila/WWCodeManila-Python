[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/WWCodeManila/Python)

# Scene 4

This scene takes place inside Aling Nena's store. You're then tasked to assist two customers: Mang Bert and Aling Tasya. The manner with which you answer their concerns will determine the succeeding scenes. 

At this point, we've already covered much of what can be learned in implementing a basic visual novel using Ren'Py. We'll only need to discuss

- [ ] Custom-defined positions 

You'll first need to add our last two characters before the `label start` block along with the other characters:

```python
define r = Character("Mang Bert")
define t = Character("Aling Tasya")
```

And these flags below where you defined the characters and before the `label start` block.

```python
define correct_change = False
define correct_item = False
```

Next, copy the assets `bg store.png` ,   `bert.png`,  `tasya.png`, `store prices.png` and `store rewards.png` from the `assets` folder into `game/images`. 

Here is the code that we'll be using. Replace the codes below the`label store` block in your `script.rpy` code and add a new block `label reward` after it:

```python
label store:
    $ storef = True
    scene bg store with fade

    show nena
    n "Thanks, [name], for helping me in the store today."
    u "It's okay Lola Nena."

    hide nena
    show bert with moveinright

    r "Good day, Aling Nena."
    n "Good day, Mang Bert. What is your business today?"
    show store prices at Position(xpos = 0.10, ypos=0.10, xanchor = 0.0, yanchor = 0.0) with dissolve
    r "I need 2 kilos of rice, 2 cans of sardines, and 1 liter of oil, please."
    u "I'll help you today, Mang Bert."

    with fade

    u "Here you go."
    "You give the items to Mang Bert."
    r "Hohoho. Thanks, [name]. Here's Php 100."
    u "Wait a minute, Mang Bert..."
    "{i}He bought 2 kilos of rice, 2 cans of sardines, and 1 liter of oil ... {w} And he gave me Php 100. That means ... {/i}"

    menu:
        "I should give him a change of {b}Php 20{/b}":
            u "Your change is Php 20."
            "You give the change to Mang Bert."
            $ correct_change = True
        "I should give him a change of {b}Php 10{/b}":
            u "Your change is Php 10."
            "You give the change to Mang Bert."
        "{b}No change{/b}":
            u "Oops. Nothing."

    if correct_change:
        "Mang Bert smiles and walks away."
        hide store prices
        hide bert with moveoutleft
    else:
        "You pocket the rest of the change."
        "Mang Bert frowns and walks away."
        hide store prices
        hide bert with moveoutleft

    with fade
    show tasya with moveinleft

    t "Good day Aling Nena and [name]."
    u "What brings you here, Aling Tasya?"
    t "I'm here to collect my reward from Aling Nena's Sari-sari store."
    u "Congratulations, Aling Tasya! What reward number did you avail?"
    show store rewards at Position(xpos = 0.90, ypos=0.10, xanchor = 1.0, yanchor = 0.0) with dissolve
    t "It's number 5."

    "You give her ... "

    menu:
        "Coke Sakto":
            "... Coke Sakto."
        "Boy Bawang":
            "... Boy Bawang."
        "Php 15 load":
            "... Php 15 load."
            $ correct_item = True

    if correct_item:
        "Aling Tasya smiles and walks away." 
        hide store rewards
        hide tasya with moveoutright
    else:
        "You keep the reward for your self."
        "Aling Tasya frowns and walks away."
        hide store rewards
        hide tasya with moveoutright

    if correct_change and correct_item:
        jump reward
    else:
        jump ending
        
label reward:
    pass
```

## Custom-defined image positions

As mentioned earlier, you can specify where in the screen an image will show instead of using the pre-defined Ren'Py positions. This can be done using the class `Position()`.

For example:

```
show store prices at Position(xpos = 0.10, ypos=0.10, xanchor = 0.0, yanchor = 0.0) with dissolve
```

In this case you'll need to set the following arguments:

`xpos` or `ypos`: Point on the screen defined by x  (horizontal) and y (vertical) positions

`xanchor` or `yanchor`: An x and y position of a point on the image. If specified, this point will be positioned on the screen at the location indicated by`xpos` and `ypos`.

Along the x-axis, `0.0` is on the extreme left, while `1.0` is on the extreme right. Along the y-axis, `0.0` is on the top-most, while a value of `1.0` is the bottom-most of the screen or image.

# Exercise

Practice with repositioning the images `store prices.png` and `store rewards.png` somewhere else in the screen by changing the keywords in the `Position()` class.

[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/WWCodeManila/Python)

