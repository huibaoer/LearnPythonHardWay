
from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    txt_input = input("> ")
    if "0" in txt_input or "1" in txt_input:
        how_much = int(txt_input);
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        txt_input = input("> ")
        if txt_input == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif txt_input == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif txt_input == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif txt_input == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    txt_input = input("> ")

    if "flee" in txt_input:
        start()
    elif "head" in txt_input:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)


def start():
    print("You are in dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    txt_input = input("> ")

    if txt_input == "left":
        bear_room()
    elif txt_input == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()