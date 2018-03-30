class Pet:
    """Beginning of a class about the goodest boy."""
        
    foodDishLevel = 100
    
    def __init__(self, name):
        self.name = name

    def add_weight(self, weight):
        self.weight = weight

    def eat(self):
        Pet.foodDishLevel -= 10
        self.weight += .03

def call():
    return 13
    
class Dog(Pet):        
    """ Dog inherits from Pet """
    
d = Dog('Dodger')

c = Dog('Gabe')

c.add_weight(10)

d.add_weight(21)

print (c.name)
print (c.weight)

c.eat()

print (c.foodDishLevel)

print (d.name)
print (d.weight)

d.eat()

print (d.foodDishLevel)

x = call()

print (x)


    
