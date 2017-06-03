from sys import exit
def gr():
    print "This room is full of gold. How much do you take?"
    n = raw_input("> ")
    if "0" in n or "1" in n:
        hm = int(n)
    else:
        dead("Man, learn to type a number.")
    if hm <50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")
def br():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bm = False
    while True:
        n = raw_input("> ")
        if n == "take honey":
            dead("The bear looks at you and slaps your face off.")
        elif n == "taunt bear" and not bm:
            print "The bear has moved from the door. You can go through it now."
            bm = True
        elif n == "taunt bear" and bm:
            dead("The bear gets pissed off and chew your leg off.")
        elif n == "open door" and bm:
            gr()
        else:
            print "I got no idea what that means."
def cr():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
    n = raw_input("> ")
    if "flee" in n:
        start()
    elif "head" in n:
        dead("Well that was tasty!")
    else:
        cr()
def dead(sth):
    print sth,"Good job!"
    exit(0)
def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"
    n = raw_input("> ")
    if n == "left":
        br()
    elif n == "right":
        cr()
    else:
        dead("You stumble around the room until you starve.")
start()
