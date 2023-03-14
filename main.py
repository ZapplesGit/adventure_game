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



day = 1
health = 10
hunger = 10
# action = "n/a"



gather_items = {
    "stick": "Combine this with a rock to make a hatchet, or with a bone to make a spear!",
    "rock": "Found it in the sand... Combine with a stick to make hatchet!",
    "aloe vera": "Plenty of it to be found around the island. Combines with Marigold to make a health mix..",
    "marigold": "Beautiful orange flower. Keep it as a memento, or combine it with Aloe Vera to make a health mix.",
    "mysterious key 1": "I wonder where this leads to...",
    "mysterious key 2": "I wonder where this leads to...",
    "blade": "Combine this with a spear to upgrade it.",
    "lucky charm": "Will give you extra luck during a fight!",
    "bone": "Combine this with a stick to make a spear!",
    "vodka": "Drink up... Or combine with cloth to make a Molotov!",
    "cloth": "Combine with Vodka to make a Molotov!",
    "grenade": "Will blow up just about anything in a fight.",
    "rope": "Combine this with a bone to make Bone Armour!"
}

inventory_items = {
    "mre": "Meal Ready to Eat. Should fill you up.",
    "stick": "Combine this with a rock to make a hatchet, or with ____ to ____!",
    "rock": "Found it in the sand... Combine with a stick to make hatchet!",
}

#for testing
# inventory_items = gather_items

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
    print("You wake up in a foreign land...")
    time.sleep(1)
    next_action()


def get_health():
    #♥♡
    health_return = ("♥"*health + "♡"*(10-health))
    return health_return


def get_hunger():
    #🍲✕
    hunger_return = ("🍲"*hunger + "✕"*(10-hunger))
    return hunger_return


def inventory():
    health_bar = get_health()
    hunger_bar = get_hunger()
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


def combinable_items(craft1, craft2):
    if craft1 == "rock" or craft2 == "rock":
        if craft1 == "stick" or craft2 == "stick":
            check = "true"
            inventory_items.update({"hatchet": "Could hit some bad guys with this..."})
            del inventory_items["rock"]
            del inventory_items["stick"]
        else:
            check = "false"
    else:
        check = "false"

    return check



def crafting():
    print("Type an item to use in crafting!")
    print(*inventory_items, sep=", ")
    print("Type X to exit.")
    while True:
        item1 = input("\n> ").lower()
        if item1 == "x":
            break
        elif item1 in inventory_items:
            print(f"Select a second item to combine with {item1}!")
            item2 = input("\n> ").lower()
            if item2 == "x":
                break
            elif item2 in inventory_items:
                if item2 != item1:
                    combinable = combinable_items(item1, item2)
                    if combinable == "true":
                        print(f"Combining {item1} and {item2}...")
                        time.sleep(1)
                        print(f"Great success! You made a {list(inventory_items)[-1]}.")
                    else:
                        print("These items do not combine!")
                else:
                    print("Please enter a different item!")
            else:
                print("Item not in inventory!")
        else:
            print("Item not in inventory!")


    next_action()

def survival():
    print("You contemplate your options...")
    print("H - Hunting \nG - Gathering \nC - Construction")
    print("Type X to exit.")

    while True:
        global inventory_items
        action = input("\n> ")
        if action == "x":
            next_action()
            break
        elif action == "h":
            print("You venture into the woods...")
            time.sleep(1)
            randomevent = random.randint(0,3)
            print(randomevent)
            if randomevent == 4:
                print("fight")
            else:
                randomevent = random.randint(0,9)
                print(randomevent)



            break
        elif action == "g":
            print("You venture into the woods...")
            time.sleep(1)
            while True:
                randomevent = random.randint(0,12)
                if list(gather_items)[randomevent] not in inventory_items:
                    inventory_items.update({list(gather_items)[randomevent]: gather_items.get(list(gather_items)[randomevent])})
                    print(f"You found a {list(inventory_items)[-1]}!")
                    time.sleep(1)
                    break
            break
        elif action == "c":
            print("construction")
        else:
            print("Please enter a valid choice!")
    next_action()

def next_action():
    print(difficulty)
    health_bar = get_health()
    hunger_bar = get_hunger()
    print(f"Day {day}")
    print(health_bar)
    print(hunger_bar)
    print("I - Inventory \nC - Crafting \nE - Exploration \nS - Survival")
    print("Type an item to use it!")

    while True:
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
            survival()
        elif action in inventory_items:
            print(f"Are you sure you want to use {action}? Y/N")
            action2 = input("\n> ").lower()
            if action2 == "y":
                #use item
                break
        else:
            print("Please select a valid choice!")


start_game()

