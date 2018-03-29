class Dog:
    """Beginning of a class about the goodest boy."""

    foodDishLevel = 100
    
    def __init__(self, name):
        self.name = name

    def add_weight(self, weight):
        self.weight = weight

    def eat(self):
        Dog.foodDishLevel -= 10

        

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
