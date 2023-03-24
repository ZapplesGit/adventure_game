# Outsider's Odyssey - The Island

"""
Brief:
"Outsider's Odyssey - The Island": The player wakes up, finding themselves stranded on a desert island inhabited by a
mysterious and isolated tribe. The tribe is distrustful of outsiders, and the main progression of the game should be
for the protagonist to uncover the secrets of the tribe, and why how they can escape the island.

The player must learn to survive on the island, hunting and gathering for food and resources, while also avoiding
dangerous predators / monsters, and natural hazards. As the player explores the island and progresses the story, they will
uncover clues and puzzles tha reveal the tribe's secrets, ultimately leading to a confrontation with the tribe's
leadership.

Additionally, the player must contend with the limited resources available on the island, managing their inventory and crafting
tools and weapons in order to survive and progress.
"""

# Import libraries and starting variables

import random
import time

day = 1
health = 10
hunger = 5

# Starting dictionaries and lists

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
    "grenade": "Will blow up just about anything in a fight."
}

inventory_items = {
    "mre": "Meal Ready to Eat. Should fill you up.",
    "stick": "Combine this with a rock to make a hatchet, or with a bone to make a spear!",
    "rock": "Found it in the sand... Combine with a stick to make hatchet!"
}

weapon_power = {
    "hatchet": 10,
    "spear": 15,
    "upgraded spear": 20,
    "molotov": 35,
    "grenade": 50
}


monster_types = ["Zombie", "Orc", "Goblin", "Dragon", "Troll", "Giant"]


def start_game():  # Choose difficulty function - difficulty not yet implemented
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


def get_health():  # Displays health bar
    # ♥♡
    global health
    if health > 10:
        health = 10
    health_return = ("♥"*health + "♡"*(10-health))
    return health_return


def get_hunger():  # Displays hunger bar
    # 🍲✕
    global hunger
    if hunger > 10:
        hunger = 10
    hunger_return = ("🍲"*hunger + "✕"*(10-hunger))
    return hunger_return


def inventory():  # Displays items in inventory
    health_bar = get_health()
    hunger_bar = get_hunger()
    print(health_bar)
    print(hunger_bar)

    print(*inventory_items, sep=", ")
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


def combinable_items(craft1, craft2):  # Checks if items are combinable / craftable
    if craft1 == "rock" or craft2 == "rock":
        if craft1 == "stick" or craft2 == "stick":
            check = True
            inventory_items.update({"hatchet": "Could hit some bad guys with this..."})
            del inventory_items["rock"]
            del inventory_items["stick"]
        else:
            check = False

    elif craft1 == "aloe vera" or craft2 == "aloe vera":
        if craft1 == "marigold" or craft2 == "marigold":
            check = True
            inventory_items.update({"health mix": "Max out your health with this!"})
            del inventory_items["aloe vera"]
            del inventory_items["marigold"]
        else:
            check = False

    elif craft1 == "stick" or craft2 == "stick":
        if craft1 == "bone" or craft2 == "bone":
            check = True
            inventory_items.update({"spear": "Could stab some bad guys with this..."})
            del inventory_items["bone"]
            del inventory_items["stick"]
        else:
            check = False

    elif craft1 == "spear" or craft2 == "spear":
        if craft1 == "blade" or craft2 == "blade":
            check = True
            inventory_items.update({"upgraded spear": "Could seriously stab some bad guys with this..."})
            del inventory_items["spear"]
            del inventory_items["blade"]
        else:
            check = False

    elif craft1 == "cloth" or craft2 == "cloth":
        if craft1 == "vodka" or craft2 == "vodka":
            check = True
            inventory_items.update({"molotov": "Could burn up some bad guys with this..."})
            del inventory_items["cloth"]
            del inventory_items["vodka"]
        else:
            check = False

    else:
        check = False

    return check


def crafting():  # Uses the combinable function to add new item in inventory from the two old items
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
                    if combinable:
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


def fight():  # The main function for fights
    global health
    print(get_health())
    monster = monster_types[random.randint(0, 5)]
    monster_health = random.randint(20, 50)
    monster_strength = random.randint(2, 4)
    fight_over = False
    print(f"Fighting a {monster}!")
    print(f"health {monster_health} strength {monster_strength}")
    print(f"Your health is {health}")
    print("\nInventory:")
    print(*inventory_items, sep=", ")
    print("\nType an item to attack with or use! Type \"hands\" to attack with your bare hands!")

    while not fight_over:
        while True:
            action = input("\n> ")

            if action in inventory_items:

                """attacking_power = weapon_power[action]

                if action in ["grenade", "health mix"]:
                    del inventory_items[action]

                break"""  # Currently working on this

                if action == "hatchet":
                    attacking_power = 10
                    break
                elif action == "spear":
                    attacking_power = 15
                    break
                elif action == "upgraded spear":
                    attacking_power = 20
                    break
                elif action == "molotov":
                    attacking_power = 35
                    del inventory_items["molotov"]
                    break
                elif action == "grenade":
                    attacking_power = 50
                    del inventory_items["grenade"]
                    break
                elif action == "health mix":
                    health = 10
                    del inventory_items["health mix"]
                else:
                    print("You cannot use this item!")
            elif action == "hands":
                attacking_power = 5
                break
            else:
                print("You don't have this item!")

        monster_damage = random.randint(1, monster_strength)
        health = health - monster_damage
        monster_health = monster_health - attacking_power

        print(get_health())
        print(f"You deal {attacking_power} damage!")
        print(f"The {monster} deals {monster_damage} damage!")
        print(f"You have {health} health. The {monster} has {monster_health} health.")

        if health < 1:
            print("Uh oh... You died!")
            quit()
            fight_over = True
        if monster_health < 1:
            print("monster die")
            fight_over = True

    print("\nFight sequence work in progress!")

    next_action()


def exploration():  # Should eventually contain the main storyline, however it currently only runs a fight
    fight()
    pass


def survival():  # Options for item gathering
    print("You contemplate your options...")
    print("H - Hunting \nG - Gathering")
    # print("Type X to exit.")

    while True:
        action = input("\n> ")
        if action == "h":
            print("You venture into the woods...")
            time.sleep(1)
            randomevent = random.randint(0, 4)
            if randomevent == 4:
                print("You are ambushed by a monster!")
                fight()
                break
            else:
                randomevent = random.randint(0, 10)
                print(randomevent)
                if -1 < randomevent < 4:
                    print("Your hunting efforts weren't fortunate... You found a dead squirrel.")
                    inventory_items.update({"squirrel meat": "🍲🍲 hunger!"})
                elif 3 < randomevent < 8:
                    print("You manage to ambush a group of ducks")

                    inventory_items.update({"duck meat": "🍲🍲🍲🍲🍲 hunger!"})
                else:
                    print("You took down a deer!")
                    inventory_items.update({"deer meat": "🍲🍲🍲🍲🍲🍲🍲🍲🍲🍲 hunger!"})

            break

        elif action == "g":
            print("You venture into the woods...")
            time.sleep(1)
            while True:
                randomevent = random.randint(0, 11)
                if list(gather_items)[randomevent] not in inventory_items:
                    inventory_items.update({list(gather_items)[randomevent]: gather_items.get(list(gather_items)[randomevent])})
                    print(f"You found a {list(inventory_items)[-1]}!")
                    time.sleep(1)
                    break
            break
        else:
            print("Please enter a valid choice!")
    next_action()


def next_action():  # Main function
    global day
    global hunger
    global health
    health_bar = get_health()
    hunger_bar = get_hunger()
    if hunger < 1:
        print("\nYou starved to death!")
        quit()
    print(f"\nDay {day}")
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
            day += 1
            hunger -= 1
            exploration()
            break
        elif action == "s":
            day += 1
            hunger -= 1
            survival()
        elif action in inventory_items:
            print(f"Are you sure you want to use {action}? Y/N")
            action2 = input("\n> ").lower()
            if action2 == "y":

                if action == "squirrel meat":
                    print("Consuming squirrel meat...")
                    time.sleep(1)
                    hunger += 2
                    del inventory_items["squirrel meat"]
                    next_action()

                if action == "duck meat":
                    print("Consuming duck meat...")
                    time.sleep(1)
                    hunger += 2
                    del inventory_items["duck meat"]
                    next_action()

                if action == "deer meat":
                    print("Consuming deer meat...")
                    time.sleep(1)
                    hunger += 10
                    del inventory_items["deer meat"]
                    next_action()

                if action == "health mix":
                    print("Consuming health mix...")
                    time.sleep(1)
                    health += 10
                    del inventory_items["health mix"]
                    next_action()

                if action == "mre":
                    print("Consuming MRE...")
                    time.sleep(1)
                    hunger += 5
                    del inventory_items["mre"]
                    next_action()

                else:
                    print("Item not found!")
        else:
            print("Please select a valid choice!")


start_game()
