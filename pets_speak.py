class Pet:
    """Beginning of a class about the goodest boy."""
        
    foodDishLevel = 100
    
    def __init__(self, name):
        self.name = name

    def add_weight(self, weight):
        self.weight = weight

    def eat(self):
        self.foodDishLevel -= 10
        self.weight += .03

    def speak(self, speak):
        self.speak = speak

def call():
    return 13
    
class Dog(Pet):        
    """ Dog inherits from Pet """
print ("Dogs:")    
d = Dog('Dodger')

c = Dog('Gabe')

c.add_weight(10)

d.add_weight(21)

print (c.name)
print (c.weight)

c.eat()

print (c.foodDishLevel)

c.speak('Bark!')


print (d.name)
print (d.weight)

d.eat()

print (d.foodDishLevel)
d.speak('Bark!')



class Cat(Pet):
    """ Cat inherits from Pet """
print ("")
print ("Cats:")

b = Cat('Milo')
b.add_weight(9)
print (b.name)
print (b.weight)
b.eat()
print (b.foodDishLevel)
b.speak('Meow!')

print ("")

a = Cat('Marley')
a.add_weight(8)
print (a.name)
print (a.weight)
a.speak('Meow!')
print (a.speak)    
