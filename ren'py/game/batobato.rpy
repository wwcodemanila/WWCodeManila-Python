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
