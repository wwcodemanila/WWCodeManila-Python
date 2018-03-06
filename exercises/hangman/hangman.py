# Hangman Game
#
# Credit to Michael Dawson's "Python Programming for the Absolute Beginner 3rd Edition"
#
# The classic game of Hangman.  The computer picks a random word
# and the player wrong to guess it, one letter at a time.  If the player
# can't guess the word in time, the little stick figure gets hanged.

# imports


# constants
HANGMAN = (
    """
     ------
     |    |
     |
     |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   -+-
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |    |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |    |
     |    |
     |   |
     |   |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |    |
     |    |
     |   | |
     |   | |
     |
    ----------
    """)

MAX_WRONG = len(HANGMAN)-1
WORDS = ("OCTOPUS", "NEMO", "STARFISH", "ORCA")  # Change these as you please


# initialize variables
word = ""                     # pick random word to be guessed
so_far = "-" * len(word)      # one dash for each letter in word to be guessed
wrong = 0                     # number of wrong guesses player has made
used = []                     # letters already guessed


print("Welcome to Hangman.  Good luck!")

# Ask for a guess while the game is not yet over
while True:
    print(HANGMAN[wrong])
    print(f"You have {MAX_WRONG-wrong} guesses left!")
    print("\nYou've used the following letters:\n", used)
    print("\nSo far, the word is:\n", so_far)

    # Get new user guess with a TWIST :P
    guess = input("\n\nEnter your guess: ")

    # Check if guess is right or wrong

    # If right, need to update user_guess

    # If wrong, need to increment wrong count

# Inform if the user won or lose

print("\nThe word was", word)

input("\n\nPress the enter key to exit.")

