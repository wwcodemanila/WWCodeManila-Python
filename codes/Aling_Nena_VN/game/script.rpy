define n = Character("Aling Nena")
define u = Character("[name]")
define b = Character("Boy")
define l = Character("Lita")
define r = Character("Mang Bert")
define t = Character("Aling Tasya")

label start:
## scene 1
    scene bg inside house 

    $ b_reward = False

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

## scene 2
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

    $ b_play = False
    $ b_store = False
    menu:
        "Lola, mamaya na. I'll play with my friends first.":
            $ b_play = True
            n "Ay naku, apo. Bahala ka."
            jump play
        "Sorry Lita and Boy, I promised my Lola I'll help her today.":
            $ b_store = True
            jump store

label store:
# scene 4
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

    $ correct_change = False
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

    $ correct_reward = False
    menu:
        "Coke Sakto":
            "... Coke Sakto."
        "Boy Bawang":
            "... Boy Bawang."
        "Php 15 load":
            "... Php 15 load."
            $ correct_reward = True

    if correct_reward:
        "Aling Tasya smiles and walks away." 
        hide store rewards
        hide tasya with moveoutright
    else:
        "You keep the reward for your self."
        "Aling Tasya frowns and walks away."
        hide store rewards
        hide tasya with moveoutright

    if correct_change and correct_reward:
        jump reward
    else:
        jump ending

label reward:
# scene 5
    with fade
    show nena

    $ b_reward = True

    n "You did well, [name]! Because you helped me a lot today, I will give you a reward."
    n "Which will it be?"

    $ baon = False
    $ b_beach = False
    menu:
        "I can give you a baon to spend with your friends.":
            $ baon = True
            u "Thanks for the allowance, Lola. I'll go play with Lita and Boy now."
            n "Go ahead, Apo. You deserve it."
            jump play
        "We'll go to the beach.":
            $ b_beach = True
            u "Let's go the beach, Lola!"
            jump beach


label beach:
# scene 6
    scene bg beach with fade

    u "Wow, Lola! The beach is so pretty."
    n "Yes, it is. Glad you like it here."

    jump ending


label ending:
# ending
    scene bg inside house with fade

    if b_reward:
        if baon:
            "You were able to spend the rest of the day with your friends Lita and Boy."
            "You bought snacks for the three of you from the allowance Aling Nena gave you."
        elif b_beach:
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
        show nena
        "Your Lola Nena is waiting for you. She doesn't look happy."
        n "Apo, I have called your Mom and Dad. They will fetch you here tomorrow."
        u "But.. but Lola..."

        if b_play:
            $ desc = "a lazy"
            n "You only played all day with your friends even though you promised to help me."
        elif b_store:
            if correct_change == False:
                $ desc = "a dishonest"
                n "Mang Bert told me that you did not give him the correct change."
                n "Instead, you pocketed the excess amount!"
            if correct_reward == False:
                $ desc = "an untrustworthy"
                n "Aling Tasya said that you didn't give her the correct reward."
                n "Instead, you kept it to your self!"
        
        n "I have no use for [desc] grandchild."

        scene bg inside house with fade

        "And just like that, your summer vacation in the province is OVER."

        "THE END"

    return

