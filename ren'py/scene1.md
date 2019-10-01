[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/WWCodeManila/Python)

# Scene 1

The first scene opens with your character interacting with Aling Nena for the first time. It is set inside Aling Nena's house. Aling Nena asks you questions which you must supply the answer to.

In implementing this scene, we'll learn about important Ren'Py *statements*:

- [ ] Label statements
- [ ] Say statements
- [ ] Defining Characters
- [ ] User inputs
- [ ] Menu statements

We'll also learn a little about how to

- [ ] use text-tags, and
- [ ] include images

Here is the code for our first scene. Copy the following code into `script.rpy` and try to run it using the Ren'Py launcher.

!> Tip: You can use  `Back` in the game screen to view the dialogue before or `Skip` to go ahead until some decision point is reached. Try these in order to view the different outcomes of your decision.

```python
define n = Character("Aling Nena")
define u = Character("[name]")

label start:
    scene bg inside house 
    
    "It's the start of summer vacation."
    "You decided to go to the province to spend some time with your lola --"
    show nena
    "Aling Nena"
    n "Apo, what's your name again?"

    "{i}Ay naku, my lola always forgets my name.{/i}"

    python:
        name = renpy.input("What is your name?").title()

    u "I'm [name], Lola Nena."
    n "Ah, yes. [name]. I remember now."
    u "..."
    n "Can you help with my errands today, apo?"

    menu:
        "Yes, Lola. You can always count on me.":
            n "Thanks Apo. I'm sure I can count on you."
        "Hmm. I rather sleep.":
            n "Really? Your Mom and Dad will hear about this!"
            u "Alright, Lola. I'll help you."
```

We'll break down this code in the following sections. Feel free to replace or edit your `script.rpy` in order to follow along.

## Label statement

First, let's consider this simplistic subset of our first scene, containing only the first part of the dialogue:

```python
label start:
    "It's the start of summer vacation."
    "You decided to go to the province to spend some time with your lola --"
    "Aling Nena"
    "Aling Nena" "Apo, what's your name again?"
    "Anna" "I'm Anna, Lola Nena."
```

The `label <description>` statement in the first line defines a specific chunk in our program. The particular statement `label start` is a *special* statement in Ren'Py denoting the start of the game. Everything else follows this statement. 

!> Thus, always start your first story block with `label start`.

## Say statements

After `label start` are *say statements*. Notice that these are indented with respect to the label statement, denoting that they are part of the `label start` *block*. In Python as well as Ren'Py, uniform indentations are important; codes following ":" in the same block must be indented with the *same number of spaces or tabs*.

There are two kinds of say statements:

One kind denotes a *narration*. Narrations consist of a single line in quotations. You can break narrations into different lines and this will show in the game in succeeding screens.

```
"It's the start of summer vacation."
"You decided to go to the province to spend some time with your lola --"
"Aling Nena"
```

The second type denotes a character speaking:

```
"Aling Nena" "Apo, what's your name again?"
"Anna" "I'm Anna, Lola Nena."
```

In this case, a space separates the character name and what he or she is saying. Both the name and dialogue is in quotations.

While this is all good and handy when coding the rest of the dialogue, it's cumbersome to always type the same names over and over again. 

## Defining characters

Fortunately, you can define characters using the `Character()` class in Ren'Py.  This is usually defined before the start block using the format: `define <variable_name> = Character("name of character")`

Let's define a variable `n`  in lieu of our first character, Aling Nena.

```python
define n = Character("Aling Nena")
label start:
    "It's the start of summer vacation."
    "You decided to go to the province to spend some time with your lola --"
    "Aling Nena"
    n "Apo, what's your name again?"
    "Anna" "I'm Anna, Lola Nena."
```

We can then use `n` in the succeeding dialogues instead of verbosely writing `"Aling Nena"` as in the 6th line:

```python
n "Apo, what's your name again?"
```

You can add more customization on how your character and its dialogue will be displayed by specifying values for keywords inside `Character()`. For example, you can  further specify a color when Aling Nena's name is displayed using `color="<hexcode>"`, e.g.

```python
define n = Character("Aling Nena", color="#FF8426")
```

This displays the character name in orange instead of the default blue. You can learn more about how the character displays can be customized [here](https://www.renpy.org/doc/html/dialogue.html#Character). Let's save this for later in this study guide. 

## Exercise

Define a variable for the character "Anna" and use this for the rest of the dialogue. 

## User inputs and text-tags

Let's challenge our self even more by requiring a user input from the player. In this case, instead of defining another character named "Anna", let's ask the player to supply a name for the character he or she is playing:

```python
define n = Character("Aling Nena")
define u = Character("[name]")
label start:
    "It's the start of summer vacation."
    "You decided to go to the province to spend some time with your lola --"
    "Aling Nena"
    n "Apo, what's your name again?"
    "{i}Ay naku, my lola always forgets my name.{/i}"
    python:
        name = renpy.input("What is your name?").title()
    u "I'm [name], Lola Nena."
    n "Ah, yes. [name]. I remember now."
    u "..."
    n "Can you help with my errands today, apo?"
```

In a usual Python script, user-inputs are passed inside the `input()` function. In Ren'Py, we do this using `renpy.input()` inside a *`python` block*.  We'll see another example of this integration in the succeeding sections.

We can then save the user input in a variable called `name` which we can treat as a string in Python. In our example, using the `.title()` method makes sure that the first letters of the character name is always capitalized.

```python
python:
    name = renpy.input("What's your name?").title()
```

Outside the `python` block, we can use this variable in a dialogue using square brackets `[]`, i.e. `[name]`. Likewise, we can use `[name]` to define a character at the start.

```python
define u = Character("[name]")
# ...
u "I'm [name], Lola Nena."
```

Code preceded by `#` is also a comment in Ren'Py just like in any Python code.

### Text-tags

You might have also noticed a line bounded by `{i}{/i}`.  This is how we can add more flair in this story by using a convention when writing character thoughts: italization. These are generally called *text-tags*  which are enclosed by `{}`.

```python
"{i}Ay naku, my lola always forgets my name.{/i}"
```

Text-tags offer further customizations on how certain texts are displayed inside the dialogue. Other examples of text-tags include:

- `{b}bold{/b}`
- `{s}strikethrough{/s}`
- `{alpha=0.5}translucent{/alpha}`
- `{color=#0080c0}color change{/color}`

We won't be discussing all Ren'Py text-tags any more than necessary in this game but you can learn more about it [here](https://www.renpy.org/doc/html/text.html?highlight=text%20tags#general-text-tags). 

Next, let's learn about one of the special features of an interactive novel: the in-game choices, which direct the flow of the story.

## Menu statement

Choices that a player makes are defined inside the `menu` block:

```python
    menu:
        "Yes, Lola. You can always count on me.":
            n "Thanks Apo. I'm sure I can count on you."
        "Hmm. I rather sleep.":
            n "Really? Your Mom and Dad will hear about this!"
            u "Alright, Lola. I'll help you."
```

The `menu` statement should still be inside a `label` statement that's why it is indented.

The choices are found in the the first level enclosed by quotations:  (1) `"Yes, Lola. You can always count on me."`  and (2) `"Hmm. I rather sleep."`

 The *consequences* are found in the next level. In this example, the consequences are simply different dialogues between the player and Aling Nena. 

Notice that uniform indentations denote statements that group together.

Last but not the least, let's include some visuals! It won't be a visual novel if it doesn't have some graphics.

## Images

There are two types of images in our first scene: One is for the background, and the others are the characters.

```python
define n = Character("Aling Nena")
define u = Character("[name]")

label start:
    scene bg inside house 
    
    "It's the start of summer vacation."
    "You decided to go to the province to spend some time with your lola --"
    show nena
    "Aling Nena"
    n "Apo, what's your name again?"
```

The `scene` statement adds a background image which persists until another `scene` statement is called, while the `show` statement puts another image on top of the background image. 

If these images are not present, Ren'Py shows some default graphics. Try to run the game from the Ren'Py launcher at this poin to see what this looks like.

Now, copy the images `bg inside house.png` and `nena.png` from the `assets` folder into `game/images`. Run the game again. 

`bg inside house` and `nena` refers to the file names inside our game folder; that is, `bg inside house.png` and `nena.png`. You can also define a custom image name and path using the `image` statement:

```python
image my_image = "/path/to/my/image.png"
# ...
show my_image
```

To hide a particular image on top of the background, you can use the `hide` statement:

```python
hide my_image
```

!> Calling the `scene` statement wipes everything from the screen and replaces it with the background image, so it won't be necessary to hide images like character images before changing the scene.

Ren'Py creates a directory called `images` when a new project is created. This is where we will put our images so we can easily find them. In practice, it doesn't matter where your images are as long as they are inside the `game` folder and are named accordingly or you have correctly put the image path using the `image` statement.

That's it! Look at the complete code again and see how easy it is to read the code and figure out the storyline.

We'll learn more about positioning and transitions between images in the next section. 

[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/WWCodeManila/Python)

