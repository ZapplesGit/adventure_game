# Outsider's Odyssey - The Island

import random
import time

'''
Brief:
"Outsider's Odyssey - The Island": The player is an outsider who finds themselves stranded on a deserted island inhabited
by a mysterious and isolated tribe. The tribe is distrustful of outsiders and has their own customs and traditions, making
it difficult for the player to communicate and form relationships with them.

The player must learn to survive on the island, hunting and gathering for food and resources, while also avoiding dangerous
predators and natural hazards. As the player explores the island, they will uncover clues and puzzles that reveal the tribe's
history and secrets, ultimately leading to a confrontation with the tribe's leadership.

The player must navigate complex moral dilemmas and make difficult choices as they interact with the tribe, deciding whether
to respect their customs or challenge them in order to achieve their objectives. The player's actions will have consequences,
affecting the tribe's perception of them and ultimately determining their fate.

Additionally, the player must contend with the limited resources available on the island, managing their inventory and crafting
tools and weapons in order to survive and progress. The player must also deal with the psychological toll of being stranded
on a deserted island, facing challenges such as loneliness, fear, and despair.
'''

difficulty = 0
day = 1
health = 10
hunger = 10
action = "n/a"
health_bar = "n/a"
hunger_bar = "n/a"


def StartGame():
    global difficulty
    print("\nWelcome to Outsider's Odyssey - The Island")
    print("Please select a difficulty level of 1-3")
    while True:
        try:
            difficulty = int(input("\n> "))
            if 0 < difficulty < 4:
                break
            else:
                print("Please enter a difficulty between 1-3!")
        except ValueError:
            print("Please enter an integer!")
    print(f"Proceeding with difficulty {difficulty}!")
    #time.sleep(1)
    print("You wake up in a foreign land... (SAMPLE INTRODUCTION SEQUENCE)")
    #time.sleep(1)
    NextAction()


def GetHealth():
    #♥♡
    global health
    global health_bar
    health_bar = ("♥"*health + "♡"*(10-health))


def GetHunger():
    #🍲✕
    global hunger
    global hunger_bar
    hunger_bar = ("🍲"*hunger + "✕"*(10-hunger))


def Inventory():
    GetHealth()
    GetHunger()
    print(health_bar)
    print(hunger_bar)


def NextAction():
    global action
    GetHealth()
    GetHunger()
    print(f"Day {day}")
    print(health_bar)
    print(hunger_bar)
    print("Time is of the essence...")
    print("I - Inventory \nC - Crafting \nE - Exploration \nS - Survival")

    while True:
        try:
            action = str(input("\n> ").lower())
            if action == "i":
                Inventory()
                break
            elif action == "c":
                print("Placeholder crafting screen")
                break
            elif action == "e":
                print("Placeholder exploration screen")
                break
            elif action == "s":
                print("Placeholder survival screen")
            else:
                print("Please select a valid choice!")
        except ValueError:
            print("Please enter a string!")

StartGame()

