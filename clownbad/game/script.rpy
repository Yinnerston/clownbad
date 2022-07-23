# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# TODO: Define colours for each character
define narrator = Character("Narrator")
define clown = Character("Clown Puppet", color="#ff2d00")
define ghost = Character("Ghost", color="#71b4ff")
define hamlet = Character("Hamlet", color="#ffdc00")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg london

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy
    with None
    show owo pog at truecenter 
    with dissolve

    # These display lines of dialogue.

    narrator " London.  A fantastical place, where there’s citywide climate control (set to constant rain), a place where you can buy a meal deal for 3.50£, and be marginally less depressed afterwards."

    menu:
        # TODO: text box to wait for joke..
        "So did anybody see that clown with the massive badonkers?  Yeah, I guess you can say that they had three honkers."

        # play sound "audio\chorus.ogg"

    return
