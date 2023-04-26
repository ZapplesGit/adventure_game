# Outsider's Odyssey - The Island

"""
Brief:
"Outsider's Odyssey - The Island": The player wakes up, finding themselves stranded on a desert island inhabited by a
mysterious and isolated tribe. The tribe is distrustful of outsiders, and the main progression of the game should be
for the protagonist to uncover the secrets of the tribe, and why how they can escape the island.

The player must learn to survive on the island, hunting and gathering for food and resources, while also avoiding
dangerous predators / monsters, and natural hazards. As the player explores the island and progresses the story, they will
uncover clues and puzzles that reveal the tribe's secrets, ultimately leading to a confrontation with the tribe's
leadership.

Additionally, the player must contend with the limited resources available on the island, managing their inventory and crafting
tools and weapons in order to survive and progress.
"""

# CURRENT KNOWN BUGS
# Gathering when you have every item breaks the game
# There is no current way to distinguishing how many items you have
# Can't currently heal in the main menu
#

# Import libraries and starting variables

import random
import time

day = 1
health = 10
hunger = 5
level = 1

# Constants

NUM_LEVELS = 8
MAX_HUNGER = 10
MAX_HEALTH = 10

FIGHT_LOSS_HEALTH = 3
ODDS_AMBUSH = 9

BANDAGE_HEALING = 5
HEALTH_MIX_HEALING = 10

SQUIRREL_MEAT_FOOD = 2
DUCK_MEAT_FOOD = 5
DEER_MEAT_FOOD = 10
MRE_FOOD = 5

# Starting dictionaries and lists

gather_items = {
    "stick": {"description": "Combine this with a rock to make a hatchet, or with a bone to make a spear!", "count": 1},
    "rock": {"description": "Found it in the sand... Combine with a stick to make hatchet!", "count": 1},
    "aloe vera": {"description": "Plenty of it to be found around the island. Combines with Marigold to make a health mix..", "count": 1},
    "marigold": {"description": "Beautiful orange flower. Keep it as a memento, or combine it with Aloe Vera to make a health mix.", "count": 1},
    "blade": {"description": "Combine this with a spear to upgrade it.", "count": 1},
    "bone": {"description": "Combine this with a stick to make a spear!", "count": 1},
    "vodka": {"description": "Drink up... Or combine with cloth to make a Molotov!", "count": 1},
    "cloth": {"description": "Combine with Vodka to make a Molotov!", "count": 1},
    "grenade": {"description": "Will blow up just about anything in a fight. Single use, will deal 50 damage.", "count": 1},
    "bandage": {"description": "Will give +5 health when used.", "count": 1}
}

inventory_items = {
    "mre": {"description": "Meal Ready to Eat. Should fill you up. Will give +5 hunger when consumed.", "count": 1},
    "stick": {"description": "Combine this with a rock to make a hatchet, or with a bone to make a spear!", "count": 1},
    "rock": {"description": "Found it in the sand... Combine with a stick to make hatchet!", "count": 1}
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

hunger_power = {
    "squirrel meat": SQUIRREL_MEAT_FOOD,
    "duck meat": DUCK_MEAT_FOOD,
    "deer meat": DEER_MEAT_FOOD,
    "mre": MRE_FOOD
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
    if health > MAX_HEALTH:
        health = MAX_HEALTH
    health_return = ("♥"*health + "♡"*(MAX_HEALTH-health))
    return health_return


def get_hunger():  # Displays hunger bar
    # 🍲✕
    # 🍗
    global hunger
    if hunger > MAX_HUNGER:
        hunger = MAX_HUNGER
    hunger_return = ("🍗"*hunger + "✕"*(MAX_HUNGER-hunger))
    return hunger_return


def inventory():  # Displays items in inventory
    health_bar = get_health()
    hunger_bar = get_hunger()

    while True:
        print("\n"+health_bar)
        print(hunger_bar)
        print(*inventory_items, sep=", ")

        for item in inventory_items:
            print(f"{item}: {inventory_items[item]['count']}")

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

    combinations = {
        ("rock", "stick"): {"result": "hatchet", "description": "Could hit some bad guys with this..."},
        ("aloe vera", "marigold"): {"result": "health mix", "description": "Max out your health with this!"},
        ("stick", "bone"): {"result": "spear", "description": "Could stab some bad guys with this... Will deal 15 damage."},
        ("spear", "blade"): {"result": "upgraded spear", "description": "Could seriously stab some bad guys with this... Will deal 20 damage."},
        ("cloth", "vodka"): {"result": "molotov", "description": "Could burn up some bad guys with this... Single use, will deal 35 damage."}
    }

    if (craft1, craft2) in combinations or (craft2, craft1) in combinations:
        check = True
        outcome = combinations.get((craft1, craft2)) or combinations.get((craft2, craft1))
        inventory_items.update({outcome["result"]: outcome["description"]})
        del inventory_items[craft1]
        del inventory_items[craft2]
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
    monster = monster_types[random.randint(0, 5)]
    monster_health = random.randint(20, 50)
    monster_strength = random.randint(2, 4)

    levels = {
        1: ["Wolf", 25, 1],
        2: ["Tribesman", 30, 2],
        3: ["Bear", 35, 2],
        4: ["Rival Tribesman", 40, 2],
        5: ["Rival Tribe Chief", 45, 3],
        6: ["Giant", 50, 3],
        7: ["Tribe Henchman", 55, 4],
        8: ["The Chief", 100, 4]
    }

    if level < (NUM_LEVELS + 1):
        monster = levels[level][0]
        monster_health = levels[level][1]
        monster_strength = levels[level][2]

    fight_over = False

    print(get_health())
    print(f"You're fighting a {monster}!")
    print(f"It has {monster_health} health, and {monster_strength} strength!")

    while not fight_over:
        while True:
            print("\nInventory:")
            print(*[element for element in inventory_items if element in weapon_power or element in healing_power], sep=", ")
            print("\nType an item to attack with or use! Type \"hands\" to attack with your bare hands!")

            action = input("\n> ")

            if action == "hands":
                attacking_power = 5
                break
            if action in inventory_items:
                if action in ["grenade", "molotov", "bandage", "health mix"]:
                    del inventory_items[action]
                if action in healing_power:
                    health += healing_power[action]
                    print(get_health())
                elif action in weapon_power:
                    attacking_power = weapon_power[action]
                    break
                else:
                    print("You can't use this item!")
            else:
                print("You don't have this item!")

        monster_damage = random.randint(1, monster_strength)
        health = health - monster_damage
        monster_health = monster_health - attacking_power

        if monster_health < 0:
            monster_health = 0

        print(get_health())
        print(f"You deal {attacking_power} damage!")
        print(f"The {monster} deals {monster_damage} damage!")
        print(f"The {monster} has {monster_health} health.")

        if health < 1 or monster_health < 1:
            fight_over = True

    if health > 0:
        print("\nYou won the fight!")
        level += 1
        time.sleep(1)
        next_action()

    else:
        print("\nUh oh... You lost the fight!")
        health = FIGHT_LOSS_HEALTH
        time.sleep(1)
        next_action()


def exploration():  # Main story function
    global level

    levels = {
        1: "\nDisoriented, you pace away from the beach and into the woods.\nYou hear distant noises, and are suddenly ambushed by a wolf!\nIf you kill the wolf, you may have a meal for tonight, if you run, you may go hungry.\n",
        2: "\nAfter that encounter with the wolf, you're shaken, but you continue into the woods.\nYou stumble upon a native tribe who lives on the island.\nThey attack! Fend the tribesman off!\n",
        3: "\nAfter that encounter with the tribe, you're shaken, but you continue into the woods.\nYou encounter the tribe again, but it seems that you have gained their respect\nThey tell you they will help you off this island, but you must prove yourself by killing a bear.\n",
        4: "\nYou've gained the trust of the tribe, but you hear a sound in the distance.\nIt's another rival tribe! They seek to kill you and your allies\nFend them off!\n",
        5: "\nThe rival tribe is back!\nAfter seeing your skill in battle, the Chief of the tribe wishes to battle!\nYou are cornered! Defeat the rival Chief!\n",
        6: "\nWith the rival chief defeated, your tribe rules over the island!\nYou hear a noise while you're out collecting firewood...\nIt's a giant! Defeat it, before it destroys the tribe!\n",
        7: "\nYou think you can rest easy now that the giant is defeated...\nWhile you're resting, you hear the chief of your tribe plotting to kill you!\nYou act fast, and attack his henchmen!\n",
        8: "\nYou have defeated his henchman, but the Chief is angry...\nHe charges at you... Defeat him to escape The Island!\n"
    }

    print(levels[level])
    time.sleep(1)
    fight()

    if level > NUM_LEVELS:
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
            event = random.randint(0, ODDS_AMBUSH)
            if event == ODDS_AMBUSH:
                print("You are ambushed by a monster!")
                fight()
                break
            else:
                event = random.randint(0, 10)
                if -1 < event < 4:
                    print("\nYour hunting efforts weren't fortunate... You found a dead squirrel.")
                    inventory_items.update({"squirrel meat": {"description": "Will give you +2 hunger when consumed!", "count": 1}})
                elif 3 < event < 8:
                    print("\nYou manage to ambush a group of ducks")

                    inventory_items.update({"duck meat": {"description": "Will give you +5 hunger when consumed!", "count": 1}})
                else:
                    print("\nYou took down a deer!")
                    inventory_items.update({"deer meat": {"description": "Fully restores hunger when consumed!", "count": 1}})
            break

        elif action == "g":
            print("You venture into the woods...")
            time.sleep(1)
            while True:
                event = random.randint(0, 9)
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
        print("\nYou're getting hungry...")
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
            if action in hunger_power:
                print(f"Are you sure you want to use {action}? Y/N")
                action2 = input("\n> ").lower()
                if action2 == "y" or "yes":
                    print(f"Consuming {action}...")
                    time.sleep(1)
                    hunger += hunger_power[action]
                    del inventory_items[action]
                    next_action()
            else:
                print("Item not edible!")
        else:
            print("Please select a valid choice!")


start_game()
