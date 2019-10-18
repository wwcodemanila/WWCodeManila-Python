[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/WWCodeManila/Python)

# Scene 3

In this scene, you played *bato-bato pik* (rock, paper, scissors) with your friends Lita and Boy who you met previously in Scene 2. 

Here, we'll learn more about

- [ ] Python equivalent statements in Ren'Py

## Exercise

Try making our own implementation of Rock, Paper, Scissors in Python first . A player wins if he or she scores 2 points first (best of three) against the computer. Only wins or loses count towards any point, ties do not change the scores. 

Replace the code in `batobato.rpy` from the previous section with the following code. Go over the `python` block carefully. We won't be discussing this particular implementation in detail, instead we'll focus on the Ren'Py code.

```python
label game:
    
    $ gamef = True

    scene bg street  with fade

    show lita at left with moveinright
    show boy at right with moveinleft

    l "Let's play bato-bato pik!"

    show boy at center with moveinright
    b "You'll play against me. Best of three!"

    python:
        from random import randint
        uscore = 0
        bscore = 0
        while uscore | bscore < 2:

            renpy.say(b, "Bato-bato pik!")

            choices = {"r": "Rock", "p": "Paper", "s": "Scissors"}
            uhand = renpy.display_menu([("Rock", "r"), ("Paper", "p"), ("Scissors", "s")])
            bhand = choices.keys()[randint(0,2)]

            uhand_c = choices[uhand]
            bhand_c = choices[bhand]

            renpy.say(b, "[bhand_c]")

            hands = (uhand, bhand)

            wins = [
                ('p', 'r'),
                ('r', 's'),
                ('s', 'p'),
            ]
            tie = False
            if hands[0] == hands[1]:
                tie = True
                result = "It's a tie!"
            elif hands in wins:
                result = "wins"
                uscore += 1
            else:
                result = "loses"
                bscore += 1

            if not tie:
                renpy.say(l, "[name] picked [uhand_c], Boy picked [bhand_c] \n [name] [result]! {w} \n Boy: [bscore], [name]: [uscore]")
            else:
                renpy.say(l, "[name] picked [uhand_c], Boy picked [bhand_c] \n [result]! {w} \n Boy: [bscore], [name]: [uscore]")

        if uscore > bscore:
            renpy.say(l, "[name] is the WINNER!")
            winner = True
        else:
            renpy.say(l, "Boy wins. [name] LOSES!")
            winner = False

    if winner:
        show boy at right with moveinleft
        l "Well done, [name]."
        b "You defeated me!"
    else:
        show boy at right with moveinleft
        b "Oh well, there's always a next time, [name]."
    
    l "Let's play another game!"
    "You spend the rest of the day playing."

    jump ending

```

In `script.py`, add the following `label` statement:

```python
label ending:
    pass
```

Try to run  the game using the Ren'Py launcher.

!> Tip: You can use  `Back` in the game screen to view the dialogue before or `Skip` to go ahead until some decision point is reached. Try these in order to view the different outcomes of your decision.

## Python equivalent statements

The `renpy.<function>` offers a convinient interface to integrate Python into your Ren'Py code. We've already used one of these when we discussed user-defined inputs in Scene 1: `renpy.input()`

You'll need to implement these equivalent statements under a `python` block.

In this code we used:

- `renpy.say()` 
- `renpy.display_menu()`

Notice that, when displaying a variable in a `renpy.say()` statement, we can just enclose it with `[]` as in:

```python
renpy.say(l, "[name] picked [uhand_c], Boy picked [bhand_c] \n [name] [result]! {w} \n Boy: [bscore], [name]: [uscore]")
```

Other equivalent statements and there usages can be found [here](https://www.renpy.org/doc/html/statement_equivalents.html). Here are some that we have already encountered in the previous sections.

- `renpy.jump()` - `jump` statement
- `renpy.scene()` - `scene` statement
- `renpy.show()` - `show` statement
- `renpy.with_statement()` - transitions, i.e. `with`

## Misc

You can actually write the code in`batobato.rpy` inside `script.rpy`. Ren'Py consolidates all `label` statements into one when it is run, so it doesn't really matter whether you partition your code into different files. In cases of large games; however, it might be more efficient or readible to divide the game into different files. This section just demonstrates that making multiple files is possible.

## Exercise

If you made your own Rock, Paper, Scissors game in Python, implement your code in this Ren'Py game instead.

You may also want to make your own mini-game (examples are: Hangman, Guess the Number, or even *Pinoy Henyo*) instead of or in addition to the one we used here. You can try coding it in Python first then integate it into this Ren'Py game using equivalent statements.

What does the text-tag `{w}{/w}` do?

What does `\n` do ?

[challenge_partial](../challenge_partial.md ':include')

[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/WWCodeManila/Python)

