[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/WWCodeManila/Python)

# Aling Nena's visual novel

We'll be going through a simple interactive game featuring Aling Nena and her *apo* (grandchild). You may have met Aling Nena during one of our basic Python study groups. 

## Plotline

This game follows the adventure of the player (you!) as Aling Nena's grandchild who have visited her in the province one summer vacation. You'll be interacting with many **characters**:

- Aling Nena, your grandmother
- Lita and Boy, your friends 
- Bert and Tasya, Aling Nena's *suki* (loyal customers) in her *sari-sari* store (a small grocery store)

The story takes places in various **scenes**:

- Inside Aling Nena's house
- Outside in the streets
- In Aling Nena's store
- The beach

Along the way, you'll have to decide what your character will do next by selecting answers in a **menu** screen. Depending on  your answers along the branching storyline, you'll either encounter a *good ending* or a *bad ending*. 

## Materials

Download the following in your local machine:

- [ ] [code for the game](game)
- [ ] [images for the game](assets)

Feel free to play this game and/or look at the codes to familiarize your self with the gameplay as well as how the code is structured.

!> If you haven't done so already, create a new Ren'Py game from the launcher called `Aling Nena VN` or whatever title you want to put in. Make sure you set the screen size to 1980 px by 720 px. 

## Scripts 

As mentioned earlier, Ren'Py creates default scripts with example codes and values when a new game is created:

- `script.rpy` - contains the main dialogue and scenes in our game. This is the file we'll be working with the most in order to create our interactive novel.
- `options.rpy` - here, we can specify some details about the game e.g. the title that will be shown in the main screen and the game version
- `gui.rpy` - this is where we can change how the game will look like including accent colors, fonts, and menu borders.
- `screens.rpy` - here we can set other properties of the game e.g. the positions of the menus and labels in each screen.

In general, Ren'Py reads all `.rpy` scripts as one so we can actually split multiple parts of the game's narration into different `.rpy` files or just write all in a single file.

# Exercise

Open the script `script.rpy`. Clear everything from this file as we will be replacing the default story with our own story.

Are you ready to learn how to make your own visual novel with Python? Let's begin!

[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/WWCodeManila/Python)

