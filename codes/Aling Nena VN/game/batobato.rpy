label play:
# scene 3

    scene bg street  with fade

    show lita at left with moveinright
    show boy at right with moveinleft

    l "Let's play bato-bato pick!"

    show boy at center with moveinright
    b "You'll play against me. Best of three!"

    python:
        from random import randint
        uscore = 0
        bscore = 0
        while uscore | bscore < 2:

            renpy.say(b, "Bato-bato pick!")

            choices = {"r": "Rock", "p": "Paper", "s": "Scissors"}
            uhand = renpy.display_menu([("Rock", "r"), ("Paper", "p"), ("Scissors", "s")])           
            bhand = choices.keys()[randint(0,2)]

            outcomes = ["loses", "wins", "It's a tie"]

            if uhand == "r":
                if bhand == "r": ri = 2
                elif bhand == "p": ri = 0
                elif bhand == "s": ri = 1
            elif uhand == "p":
                if bhand == "r": ri = 1
                elif bhand == "p": ri = 2
                elif bhand == "s": ri = 0
            elif uhand == "s":
                if bhand == "r": ri = 0
                elif bhand == "p": ri = 1
                elif bhand == "s": ri = 2

            result = outcomes[ri]
            
            bhand_c = choices[bhand]
            renpy.say(b, "[bhand_c]") 
            
            if ri == 1:
                uscore += 1
            elif ri == 0:
                bscore += 1

            if ri != 2:    
                renpy.say(l, "[name] [result]! Boy: [bscore], [name]: [uscore]")
            else:
                renpy.say(l, "[result]! Boy: [bscore], [name]: [uscore]")

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
