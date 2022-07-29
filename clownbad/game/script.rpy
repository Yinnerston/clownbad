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
    menu:
        "You try to tell a joke (it’s not very funny)":
            "So did anybody see that clown with the massive badonkers?  Yeah, I guess you can say that they had three honkers."

    narrator " London.  A fantastical place, where there’s citywide climate control (set to constant rain), a place where you can buy a meal deal for 3.50£, and be marginally less depressed afterwards."

    menu:
        "Chorus - was there even a chorus in the play?":
            # TODO: Add chorus
            # play sound "audio\chorus.ogg"
            "sussy"
    menu:
        "it was - where was this play set?":
            "In uhh in Denmark?  I think it’s set in Denmark."
        "oh god what do I say I failed geography":
            "In Swe - no, it was Denmark"
        "performance anxiety":
            "In..."
    menu:
        "Didn’t Hamlet’s father completely OWN another King in war or something":
            "In Denmark, a kingdom fighting for survival against a Norwegian invasion,"
        "the bad old days, right?  Surely something nasty would’ve happened":
            "In Denmark, a land struggling under the weight of a plague,"
        "where even is Denmark?":
            "Denmark…"
            # Insert funny viking imagery here?
    menu:
        "Surely people would’ve liked the old King, right?":
            "tragedy struck once more when the King mysteriously passed away."
        "he died, right?  The king, that is":
            "the King passed away, sending the Kingdom into further turmoil."
        "Uhhh":
            "… the old king just… died?"
    menu:
        "honestly, if I were the King, I would’ve just taken the L, instead of, you know, haunting the castle like a little bitch":
            show L ratio at truecenter
            "Tales soon spread of an apparition stalking the battlements."
        "god imagine dying, only to haunt Denmark":
            "Rumours arose that a phantom, bearing the King’s own armour, haunted the battlements."
        "spooky ghost time":
            "the king was seen on the battlements - in a very not-alive manner."
    # TODO: Add button on thames
    menu:
        "this must be where Hamlet shows up":
            "The king’s son, Hamlet, went to confront the spectre."
        "Hamlet pops up here":
            "Hamlet confronted the ghost."
        "This play’s called Hamlet, he must show up around now":
            "Hamlet chatted with his ghost dad for a bit."
        "slurps up that viscous thamussy":
            # play beatdrop.mp3
            # show viscous thamussy
            # with dissolve / rotate?
            "You have perished from too much thamussy."
            jump you_died
    scene bg hamlet
    menu:
        "the ghost went all like “avveeeeengge me hamlettttt":
            "The ghost told Hamlet of his poisoning at the hands of his brother."
        "What did the ghost tell Hamlet?":
            "The ghost accused his brother of poisoning him."
        "the ghost was all like “my brother killed me oooooOOOOoooH":
            "the ghost was all like “my brother killed me oooooOOOOoooH"
    
    menu :
        "I swear to god, Hamlet gets all hesitant-about-killing-his-uncle-y":
            "Hamlet carefully considered the apparition’s words."
        "oh god oh god I don’t remember what Hamlet does":
            "Hamlet didn’t quite know what to make of it all."
        "Hamlet…I dunno…he mopes around":
            "Hamlet did…Hamlet things."
    default route_a = False
    menu:
        "and then?  And then?  He just gets everyone killed, right?":
            $ route_a = True
            "Hamlet then gets everyone killed."
        "ok and then everybody dies":
            "Ok and then everybody dies because of Hamlet."
        "I need to end this quick, that Englishman over there, I think he’s got a knife":
            "Hamlet then kills everyone, including himself."
        
    if route_a:
        jump route_a_post
    else:
        jump close_curtains

    label route_a_post:
        pass
    ghost "Curses, why did I have to haunt this battlement of all places?  I knew I should’ve haunted that orchard."
    hamlet "Who’s there?"
    ghost "Ah, Hamlet, my son, look, I need you to do me a favour - right?  Kill your uncle - the twat deserves it after he poured poison down my ear."
    hamlet "I…what"
    # do close curtains transformation
    # scene bg curtains
    narrator "A few murders, couple of gaslighting incidents and a suicide later…"
    hamlet "Uncle, I have come to avenge my father"
    # puppet bash animation
    jump end

    
    # Only die for horny ofc
    label you_died:
        scene bg death
        # play sad_trombone.mp3
        # ^ do-do-doo-dooo
        # funny skeleton
    label close_curtains:
        scene bg curtains
        # define transform for closing curtains
    label end:
        pass
    return
