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

