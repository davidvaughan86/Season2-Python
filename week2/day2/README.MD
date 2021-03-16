# updating dictionaries

aDict = ['a':1, 'b':2, 'c':3]

def updateDict():
    aDict['key'] += 1

    this would update the key pair value by 1 if a key name is passed in

# defining within the scope
for a while loop, all things contained within the scope are ran

# creating classes

class (variable):

aDict = ['a':1, 'b':2, 'c':3]

class (variable):
    def __init__(self):
        self.a = 1
        self.b = 2

x = (class variable) ()
# this is called dot notation
print(value.key)


ex: 
class Spider:
    def __init__(self):
        self.name = 'spidey'
        self.str = '20'
        self.defense = '10'
        self.hp = '100'
    pass

spidey = Spider()
print(spidey.name)
venm = Spider()

# we always define 'self' first
ex:
class Spider:
    def __init__(self, name, str, defense, hp):
        self.name = 'spidey'
        self.str = '20'
        self.defense = '10'
        self.hp = '100'
    pass

spidey = Spider()
print(spidey.name)
venom = Spider()
print(venom.str)

# we pass in the rest of our self. as arguments/parameters
ex:
class Spider:
    def __init__(self, name, str, defense, hp):
        self.name = name
        self.str = str
        self.defense = defense
        self.hp = hp
    pass


# we pass in the rest of our arguments into the function called
ex:
class Spider:
    def __init__(self, name, str, defense, hp):
        self.name = name
        self.str = str
        self.defense = defense
        self.hp = hp
    pass

spidey = Spider(name, str, defense, hp)
print(spidey.name)
venom = Spider(name, str, defense, hp)
print(venom.str)

adding new classes is as simple as 
(newclass) = (classname)(pass in the class dot notations)
carnage = Spider(name, str, defense, hp)

# functions defined inside of a class are called methods
    those methods affect and are used on that unique instance of that class.
    class Spider:
    
    def __init__(self, name, strength, defense, hp):
        self.name = name
        self.strength = strength
        self.defense = defense
        self.hp = hp


        def feed (self):
            print('eating')
            self.strength+= 5

    spidey.feed() this function is called with the variable, dot notation, function.

    the output will increase the instance of spider(spidey) strength by 5

## dictionaries can be made into classes. Classes can have methods to alter them

methods can have access to functions we declare outside of the class. 
This requires a global scope