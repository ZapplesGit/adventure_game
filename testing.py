import random

"""
var1 = 4
var2 = 4
var3 = 5


def funct(num1, num2):
    if num1 == num2:
        output = "These numbers are equal!"
    else:
        output = "These numbers are not equal!"
    return output


final = funct(var1, var2)

print(final)

print(funct(var1, var3))


hunger = 5

def get_hunger():
    a = hunger
    print(f"var is {a}")
    a = a + 2
    hunger_return = ("🍲"*a + "✕"*(10-a))
    return hunger_return

h = get_hunger()

print(f"final hunger {h}")


# Python3 program to
# demonstrate instantiating
# a class


class Dog:

    # A simple class
    # attribute
    attr1 = "mammal"
    attr2 = "dog"

    # A sample method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)


# Driver code
# Object instantiation
Rodger = Dog()

# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()


# Replacing "if" statements

level = 1

for i in range(1,6):

    levels = {
        1: ["Wolf", 25, 1],
        2: ["Tribesman", 30, 2],
        3: ["Bear", 35, 2],
        4: ["Rival Tribesman", 40, 2],
        5: ["Rival Tribe Chief", 45, 3],
        6: ["Giant", 50, 3]
    }

    monster = levels[level][0]
    monster_health = levels[level][1]
    monster_strength = levels[level][2]

    print(level)
    print(monster)
    print(monster_health)
    print(monster_strength)

    level += 1
"""

inventory_items = {
    "mre": {"description": "Meal Ready to Eat. Should fill you up. Will give +5 hunger when consumed.", "count": 1},
    "stick": {"description": "Combine this with a rock to make a hatchet, or with a bone to make a spear!", "count": 1},
    "rock": {"description": "Found it in the sand... Combine with a stick to make hatchet!", "count": 1}
}

gather_items = {
    "stick": {"description": "Combine this with a rock to make a hatchet, or with a bone to make a spear!", "count": 1},
    "rock": {"description": "Found it in the sand... Combine with a stick to make hatchet!", "count": 1},
    "balls": {"description": "ball!", "count": 1}
}


# print(inventory_items["mre"]["count"])

event = random.randint(0,2)

if list(gather_items)[event] not in inventory_items:
    print("ADDING ITEM")
    inventory_items.update({list(gather_items)[event]: gather_items.get(list(gather_items)[event])})
else:
    print("ADDING NUM")
    inventory_items[list(gather_items)[event]]["count"] += 1
    # This should add to the number of a specific item


print(f"You found a {list(gather_items)[event]}!")

for item in inventory_items:
    print(f"{item}: {inventory_items[item]['count']} - {inventory_items[item]['description']} ")
