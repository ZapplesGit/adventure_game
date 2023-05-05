# Outsider's Odyssey - The Island
# Aidan Gould-Pretorius

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

# Import libraries and starting variables

import random
import time

day = 1
health = 0
hunger = 0
level = 1
difficulty = 0

# Constants

MIN_DIFFICULTY = 1
MAX_DIFFICULTY = 3

NUM_LEVELS = 8
MAX_HUNGER = 10
MAX_HEALTH = 10

FIGHT_LOSS_HEALTH = 3  # How much health you are set to after losing a fight
ODDS_AMBUSH = 9  # Decrease this number to increase the likelihood of an ambush

BANDAGE_HEALING = 5
HEALTH_MIX_HEALING = 10
SQUIRREL_MEAT_FOOD = 2
DUCK_MEAT_FOOD = 5
DEER_MEAT_FOOD = 10
MRE_FOOD = 5

# Dictionaries and lists

gather_items = {  # The items which you can possibly gather from my gather function
    "stick": "Combine this with a rock to make a hatchet, or with a bone to make a spear!",
    "rock": "Found it in the sand... Combine with a stick to make hatchet!",
    "aloe vera": "Plenty of it to be found around the island. Combines with Marigold to make a health mix..",
    "marigold": "Beautiful orange flower. Keep it as a memento, or combine it with Aloe Vera to make a health mix.",
    "blade": "Combine this with a spear to upgrade it.",
    "bone": "Combine this with a stick to make a spear!",
    "vodka": "Drink up... Or combine with cloth to make a Molotov!",
    "cloth": "Combine with Vodka to make a Molotov!",
    "grenade": "Will blow up just about anything in a fight. Single use, will deal 50 damage.",
    "bandage": "Will give +5 health when used."
}

inventory_items = {  # These are the items you start with, this dictionary will change throughout the game
    "mre": "Meal Ready to Eat. Should fill you up. Will give +5 hunger when consumed.",
    "stick": "Combine this with a rock to make a hatchet, or with a bone to make a spear!",
    "rock": "Found it in the sand... Combine with a stick to make hatchet!"
}

weapon_power = {  # This is the amount of damage each weapon does
    "hatchet": 10,
    "spear": 15,
    "upgraded spear": 20,
    "molotov": 35,
    "grenade": 50
}

healing_power = {  # This is the amount of healing each healing aspect of the game does
    "health mix": 10,
    "bandage": 5
}

hunger_power = {  # This is the amount of hunger you get back for eating food, can be changed in constants above
    "squirrel meat": SQUIRREL_MEAT_FOOD,
    "duck meat": DUCK_MEAT_FOOD,
    "deer meat": DEER_MEAT_FOOD,
    "mre": MRE_FOOD
}

combinations = {  # The possible crafting combinations
    ("rock", "stick"): {"result": "hatchet", "description": "Could hit some bad guys with this..."},
    ("aloe vera", "marigold"): {"result": "health mix", "description": "Max out your health with this!"},
    ("stick", "bone"): {"result": "spear", "description": "Could stab some bad guys with this... Will deal 15 damage."},
    ("spear", "blade"): {"result": "upgraded spear", "description": "Could seriously stab some bad guys with this... Will deal 20 damage."},
    ("cloth", "vodka"): {"result": "molotov", "description": "Could burn up some bad guys with this... Single use, will deal 35 damage."}
}

levels = {  # Format - Level: ["Name of enemy", Health of enemy, Strength of enemy]
    1: ["Wolf", 25, 1],
    2: ["Tribesman", 30, 2],
    3: ["Bear", 35, 2],
    4: ["Rival Tribesman", 40, 2],
    5: ["Rival Tribe Chief", 45, 3],
    6: ["Giant", 50, 3],
    7: ["Tribe Henchman", 55, 4],
    8: ["The Chief", 100, 4]
}

level_text = {  # The game's storyline is kept in this dictionary, on a level-by-level basis.
    1: "\nDisoriented, you pace away from the beach and into the woods.\nYou hear distant noises, and are suddenly ambushed by a wolf!\nIf you kill the wolf, you may have a meal for tonight, if you run, you may go hungry.\n",
    2: "\nAfter that encounter with the wolf, you're shaken, but you continue into the woods.\nYou stumble upon a native tribe who lives on the island.\nThey attack! Fend the tribesman off!\n",
    3: "\nAfter that encounter with the tribe, you're shaken, but you continue into the woods.\nYou encounter the tribe again, but it seems that you have gained their respect\nThey tell you they will help you off this island, but you must prove yourself by killing a bear.\n",
    4: "\nYou've gained the trust of the tribe, but you hear a sound in the distance.\nIt's another rival tribe! They seek to kill you and your allies!\nFend them off!\n",
    5: "\nThe rival tribe is back!\nAfter seeing your skill in battle, the Chief of the tribe wishes to battle!\nYou are cornered! Defeat the rival Chief!\n",
    6: "\nWith the rival chief defeated, your tribe rules over the island!\nYou hear a noise while you're out collecting firewood...\nIt's a giant! Defeat it, before it destroys the tribe!\n",
    7: "\nYou think you can rest easy now that the giant is defeated...\nWhile you're resting, you hear the chief of your tribe plotting to kill you!\nYou act fast, and attack his henchmen!\n",
    8: "\nYou have defeated his henchman, but the Chief is angry...\nHe charges at you... Defeat him to escape The Island!\n"
}

# The types of monsters that can randomly appear in an ambush
monster_types = ["Zombie", "Orc", "Goblin", "Dragon", "Troll", "Giant"]

# (for testing)
# inventory_items.update(gather_items)


def start_game():  # Choose difficulty function - difficulty not yet implemented
    global health
    global hunger
    global difficulty
    print("\nWelcome to Outsider's Odyssey - The Island")
    print(f"Please enter a difficulty between {MIN_DIFFICULTY}-{MAX_DIFFICULTY}")
    while True:
        try:
            difficulty = int(input("\n> "))
            if MIN_DIFFICULTY-1 < difficulty < MAX_DIFFICULTY+1:
                break
            else:
                print(f"Please enter a difficulty between {MIN_DIFFICULTY}-{MAX_DIFFICULTY}!")
        except ValueError:
            print("Please enter an integer!")
    print(f"Proceeding with difficulty {difficulty}!")
    print("\nYou wake up in a foreign land...\nHunt for food or gather resources to craft weapons, or go exploring"
          " to uncover the mysteries of The Island...")
    health = (4-difficulty)*3
    hunger = (4-difficulty)*3
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


def fight(ambush):  # The main function for fights
    global health
    global level
    fight_over = False
    attacking_power = 0
    monster = monster_types[random.randint(0, 5)]
    monster_health = random.randint(20, 40)
    monster_strength = random.randint(2, 3)

    if not ambush:
        monster = levels[level][0]
        monster_health = levels[level][1]
        monster_strength = levels[level][2]

    print(get_health())
    print(f"You're fighting a {monster}!")
    print(f"It has {monster_health} health, and {monster_strength} strength!")

    while not fight_over:
        while True:
            print("\nInventory:")
            print(*[element for element in inventory_items if element in weapon_power or element in healing_power], sep=", ")
            print("\nType an item to attack with or use! Type \"hands\" to attack with your bare hands!"
                  " Type \"run\" to run away!")
            action = input("\n> ")
            if action == "run":
                print("You ran away!")
                fight_over = True
                next_action()
                break
            elif action == "hands":
                attacking_power = 5
                break
            elif action in inventory_items:
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

        if level > NUM_LEVELS:
            print("The Chief falls, and you know that you are finally free. With nothing to stop you, you devote")
            print("the next few weeks to building a boat and escaping. Eventually, you cobble together the resources.")
            print("You set sail, with no clue as to what lies in your future...")
            time.sleep(5)
            quit()

        next_action()

    else:
        print("\nUh oh... You lost the fight!")
        health = FIGHT_LOSS_HEALTH
        time.sleep(1)
        next_action()


def exploration():  # Main story function. This function has become very small after moving my
    # Main story text into a dictionary at the beginning of the program.
    global level

    print(level_text[level])
    time.sleep(1)
    fight(False)


def survival():  # Options for item gathering and hunting
    global day
    global hunger
    print("You contemplate your options...")
    print("H - Hunting \nG - Gathering")
    print("Type X to exit.")

    while True:
        action = input("\n> ").lower()
        if action == "h" or action == "hunt":
            day += 1
            hunger -= 1
            print("You venture into the woods...")
            time.sleep(1)
            event = random.randint(0, ODDS_AMBUSH)
            if event == ODDS_AMBUSH:
                print("You are ambushed by a monster!")
                time.sleep(1)
                fight(True)
                break
            else:
                if not {"squirrel meat", "duck meat", "deer meat"}.issubset(set(inventory_items)):
                    event = random.randint(0, 2)
                    if event == 0 and "squirrel meat" not in inventory_items:
                        print("\nYour hunting efforts weren't fortunate... You found a dead squirrel.")
                        inventory_items.update({"squirrel meat": "Will give you +2 hunger when consumed!"})
                    elif event == 1 and "duck meat" not in inventory_items:
                        print("\nYou manage to ambush a group of ducks!")
                        inventory_items.update({"duck meat": "Will give you +5 hunger when consumed!"})
                    else:
                        print("\nYou took down a deer!")
                        inventory_items.update({"deer meat": "Fully restores hunger when consumed!"})
                else:
                    print("Uh oh! It looks like your pockets are full!")
                    day -= 1
                    hunger += 1
                    break
            time.sleep(1)
            break

        elif action == "g" or action == "gather":
            day += 1
            hunger -= 1
            print("You venture into the woods...")
            time.sleep(1)
            while True:
                event = random.randint(0, 9)

                # Used .issubset and turned the dictionaries into sets to
                # check if all the items in gather_items are in inventory_items

                if not set(gather_items).issubset(set(inventory_items)):
                    if list(gather_items)[event] not in inventory_items:
                        inventory_items.update({list(gather_items)[event]: gather_items.get(list(gather_items)[event])})
                        print(f"You found a {list(inventory_items)[-1]}!")
                        time.sleep(1)
                        break
                else:
                    print("Uh oh! It looks like your pockets are full!")
                    day -= 1
                    hunger += 1
                    break
            break
        elif action == "x" or action == "exit":
            break
        else:
            print("Please enter a valid choice!")
    next_action()


def next_action():  # Main function, home screen
    global day
    global hunger
    global health
    health_bar = get_health()
    hunger_bar = get_hunger()
    if hunger <= 0:
        print("\nYou starved to death!")
        print("Press Y to replay the game.")
        answer = str(input("\n> ").lower())
        if answer == "y":
            start_game()
        else:
            quit()
    if hunger <= 4:
        print("\nYou're getting hungry...")

    while True:
        print(f"\nDay {day}")
        print(health_bar)
        print(hunger_bar)
        print("I - Inventory \nC - Crafting \nE - Exploration \nS - Survival")
        print("Or, type an item to use it!")
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
            survival()

        elif action in inventory_items:  # This checks if the input is an item that can be used
            if action in hunger_power or action in healing_power:
                print(f"Are you sure you want to use {action}? Y/N")
                while True:
                    action2 = input("\n> ").lower()
                    if action2 == "y" or action2 == "yes":
                        print(f"Consuming {action}...")
                        time.sleep(1)
                        if action in hunger_power:
                            hunger += hunger_power[action]
                        else:
                            health += healing_power[action]
                        del inventory_items[action]
                        next_action()
                        break
                    elif action2 == "n" or action2 == "no":
                        print(f"You decided against using {action}!")
                        break
                    else:
                        print("Please select Y or N!")
            else:
                print("Item not edible!")
        else:
            print("Please select a valid choice!")


start_game()  # Starts the game
