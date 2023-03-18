"""var1 = 69
var2 = 69


def funct(num1, num2):
    if num1 == num2:
        output = "Great success!"
    else:
        output = "No success :("
    return output


final = funct(var1, var2)


print(final)

print(funct(var1, var2))


hunger = 5

def get_hunger():
    a = hunger
    print(f"var is {a}")
    a = a + 2
    hunger_return = ("🍲"*a + "✕"*(10-a))
    return hunger_return

h = get_hunger()

print(f"final hunger {h}")
"""

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
