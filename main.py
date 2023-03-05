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
health = 5
hunger = 5
# action = "n/a"
health_bar = "n/a"
hunger_bar = "n/a"

inventory_items = {
    'rock': 'Found it in the sand... Combine with Stick to make hatchet!',
    'mre': 'Meal Ready to Eat. Should fill you up.',
}

# inventory_items.update({"example": "example"})

def start_game():
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
    next_action()


def get_health():
    #♥♡
    global health_bar
    health_bar = ("♥"*health + "♡"*(10-health))


def get_hunger():
    #🍲✕
    global hunger_bar
    hunger_bar = ("🍲"*hunger + "✕"*(10-hunger))


def inventory():
    get_health()
    get_hunger()
    print(health_bar)
    print(hunger_bar)

    print(*inventory_items, sep=", ")


#    for keys, value in inventory_items.items():
#        print(keys)

    print("Type an item to learn more. Type X to exit.")

    while True:
        action = input("\n> ").lower()
        if action == "x":
            break
        elif action in inventory_items:
            print(inventory_items[action])
        else:
            print("Invalid input.")

    next_action()

def crafting():
    print("Type an item to use in crafting!")
    print(*inventory_items, sep=", ")
    print("Type X to exit.")

    while True:
        action = input("\n> ").lower()
        if action == "x":
            break
        elif action in inventory_items:
            print(f"Select a second item to combine with {action}!")
            action2 = input("\n> ").lower()
            if action2 == "x":
                break
            elif action2 in inventory_items:
                if action2 != action:
                    print(action)
                    print(action2)
                    print("Operation success")
                else:
                    print("Please enter a different item!")
            else:
                print("Item not in inventory!")
        else:
            print("Item not in inventory!")


    next_action()



def next_action():
    get_health()
    get_hunger()
    print(f"Day {day}")
    print(health_bar)
    print(hunger_bar)
    print("I - Inventory \nC - Crafting \nE - Exploration \nS - Survival")
    print("Type an item to use it!")

    while True:
        try:
            action = str(input("\n> ").lower())
            if action == "i":
                inventory()
                break
            elif action == "c":
                crafting()
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

start_game()

