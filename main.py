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
level = 1

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
    "grenade": "Will blow up just about anything in a fight. Single use, will deal 50 damage.",
    "bandage": "Will give +5 health."
}

inventory_items = {
    "mre": "Meal Ready to Eat. Should fill you up. +5 hunger.",
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

healing_power = {
    "health mix": 10,
    "bandage": 5
}

monster_types = ["Zombie", "Orc", "Goblin", "Dragon", "Troll", "Giant"]

# (for testing)
# inventory_items = gather_items


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
    # 🍗
    global hunger
    if hunger > 10:
        hunger = 10
    hunger_return = ("🍗"*hunger + "✕"*(10-hunger))
    return hunger_return


def inventory():  # Displays items in inventory
    health_bar = get_health()
    hunger_bar = get_hunger()

    while True:
        print("\n"+health_bar)
        print(hunger_bar)
        print(*inventory_items, sep=", ")
        print("Type an item to learn more. To use an item, type X to exit.")
        action = input("\n> ").lower()
        if action == "x":
            break
        elif action in inventory_items:
            print(inventory_items[action])
            time.sleep(1)
        else:
            print("Invalid input.")

    next_action()


def combinable_items(craft1, craft2):  # Checks if items are combinable / craft-able
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
            inventory_items.update({"spear": "Could stab some bad guys with this... Will deal 15 damage."})
            del inventory_items["bone"]
            del inventory_items["stick"]
        else:
            check = False

    elif craft1 == "spear" or craft2 == "spear":
        if craft1 == "blade" or craft2 == "blade":
            check = True
            inventory_items.update({"upgraded spear": "Could seriously stab some bad guys with this... Will deal 20 damage."})
            del inventory_items["spear"]
            del inventory_items["blade"]
        else:
            check = False

    elif craft1 == "cloth" or craft2 == "cloth":
        if craft1 == "vodka" or craft2 == "vodka":
            check = True
            inventory_items.update({"molotov": "Could burn up some bad guys with this... Single use, will deal 35 damage."})
            del inventory_items["cloth"]
            del inventory_items["vodka"]
        else:
            check = False

    else:
        check = False

    return check


def crafting():  # Uses the combinable function to add new item in inventory from the two old items
    while True:
        print("\nType an item to use in crafting!")
        print(*inventory_items, sep=", ")
        print("Type X to exit.")
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
                        time.sleep(1)
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
    global level
    print(get_health())
    monster = monster_types[random.randint(0, 5)]
    monster_health = random.randint(20, 50)
    monster_strength = random.randint(2, 4)

    if level == 1:
        monster = "Wolf"
        monster_health = 25
        monster_strength = 1

    if level == 2:
        monster = "Tribesman"
        monster_health = 30
        monster_strength = 2

    if level == 3:
        monster = "Bear"
        monster_health = 35
        monster_strength = 2

    if level == 4:
        monster = "Rival Tribesman"
        monster_health = 40
        monster_strength = 2

    if level == 5:
        monster = "Rival Tribe Chief"
        monster_health = 45
        monster_strength = 3

    if level == 6:
        monster = "Giant"
        monster_health = 50
        monster_strength = 3

    if level == 7:
        monster = "Tribesman warrior"
        monster_health = 55
        monster_strength = 3

    if level == 8:
        monster = "The Chief"
        monster_health = 70
        monster_strength = 4

    fight_over = False

    print(f"You're fighting a {monster}!")
    print(f"It has {monster_health} health, and {monster_strength} strength!")

    while not fight_over:
        print("\nInventory:")
        # print(*inventory_items, sep=", ")
        print(*[element for element in inventory_items if element in weapon_power or element in healing_power], sep=", ")
        print("\nType an item to attack with or use! Type \"hands\" to attack with your bare hands!")
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
                elif action == "bandage":
                    health += 5
                    del inventory_items["bandage"]
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
        print(f"The {monster} has {monster_health} health.")

        if health < 1:
            print("Uh oh... You died!")
            quit()
            fight_over = True
        if monster_health < 1:
            print("monster die")
            fight_over = True

    print("\nYou won the fight!")
    level += 1
    time.sleep(1)
    next_action()


def exploration():  # Should eventually contain the main storyline, however it currently only runs a fight
    global level
    if level == 1:
        print("\nDisoriented, you pace away from the beach and into the woods.")
        print("You hear distant noises, and are suddenly ambushed by a wolf!")
        print("If you kill the wolf, you may have a meal for tonight, if you run, you may go hungry.\n")
        time.sleep(1)
        fight()
    pass

    if level == 2:
        print("\nAfter that encounter with the wolf, you're shaken, but you continue into the woods.")
        print("You stumble upon a native tribe who lives on the island.")
        print("They attack! Fend the tribesman off!\n")
        time.sleep(1)
        fight()
    pass

    if level == 3:
        print("\nAfter that encounter with the tribe, you're shaken, but you continue into the woods.")
        print("You encounter the tribe again, but it seems that you have gained their respect")
        print("They tell you they will help you off this island, but you must prove yourself by killing a bear.\n")
        time.sleep(1)
        fight()
    pass

    if level == 4:
        print("\nYou've gained the trust of the tribe, but you hear a sound in the distance.")
        print("It's another rival tribe! They seek to kill you and your allies")
        print("Fend them off!")
        time.sleep(1)
        fight()
    pass

    if level == 5:
        print("\nThe rival tribe is back!")
        print("After seeing your skill in battle, the Chief of the tribe wishes to battle!")
        print("You are cornered! Defeat the rival Chief!")
        time.sleep(1)
        fight()
    pass

    if level == 6:
        print("\nWith the rival chief defeated, your tribe rules over the island!")
        print("You hear a noise while you're out collecting firewood...")
        print("It's a giant! Defeat it, before it destroys the tribe!")
        time.sleep(1)
        fight()
    pass

    if level == 7:
        print("\nYou think you can rest easy now that the giant is defeated...")
        print("While you're resting, you hear the chief of your tribe plotting to kill you!")
        print("You act fast, and attack his henchmen!")
        time.sleep(1)
        fight()
    pass

    if level == 8:
        print("\nYou have defeated his henchman, but the Chief is angry...")
        print("He charges at you... Defeat him to escape The Island!")
        time.sleep(1)
        fight()

    if level > 8:
        fight()


def survival():  # Options for item gathering
    print("You contemplate your options...")
    print("H - Hunting \nG - Gathering")
    # print("Type X to exit.")

    while True:
        action = input("\n> ")
        if action == "h":
            print("You venture into the woods...")
            time.sleep(1)
            event = random.randint(0, 4)
            if event == 4:
                print("You are ambushed by a monster!")
                fight()
                break
            else:
                event = random.randint(0, 10)
                print(event)
                if -1 < event < 4:
                    print("Your hunting efforts weren't fortunate... You found a dead squirrel.")
                    inventory_items.update({"squirrel meat": "+2 hunger!"})
                elif 3 < event < 8:
                    print("You manage to ambush a group of ducks")

                    inventory_items.update({"duck meat": "+5 hunger!"})
                else:
                    print("You took down a deer!")
                    inventory_items.update({"deer meat": "Fully restores hunger when consumed!"})
            break

        elif action == "g":
            print("You venture into the woods...")
            time.sleep(1)
            while True:
                event = random.randint(0, 12)
                if list(gather_items)[event] not in inventory_items:
                    inventory_items.update({list(gather_items)[event]: gather_items.get(list(gather_items)[event])})
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
    if hunger <= 0:
        print("\nYou starved to death!")
        quit()
    if hunger <= 4:
        print("You're getting hungry...")
    print(f"\nDay {day}")
    print(health_bar)
    print(hunger_bar)
    print("I - Inventory \nC - Crafting \nE - Exploration \nS - Survival")
    print("Or, type an item to use it!")

    while True:
        action = str(input("\n> ").lower())
        if action == "i" or action == "inventory":
            inventory()
            break
        elif action == "c" or action == "craft" or action == "crafting":
            crafting()
            break
        elif action == "e" or action == "explore" or action == "exploration":
            day += 1
            hunger -= 1
            exploration()
            break
        elif action == "s" or action == "survival" or action == "survive":
            day += 1
            hunger -= 1
            survival()
        elif action in inventory_items:
            print(f"Are you sure you want to use {action}? Y/N")
            action2 = input("\n> ").lower()
            if action2 == "y" or "yes":

                if action == "squirrel meat":
                    print("Consuming squirrel meat...")
                    time.sleep(1)
                    hunger += 2
                    del inventory_items["squirrel meat"]
                    next_action()

                if action == "duck meat":
                    print("Consuming duck meat...")
                    time.sleep(1)
                    hunger += 5
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

                if action == "bandage":
                    print("Using bandage...")
                    time.sleep(1)
                    health += 5
                    del inventory_items["bandage"]
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
