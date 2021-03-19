class Spider:
    def __init__(self, name, strength, defense, hp):
        self.name = name
        self.strength = strength
        self.defense = defense
        self.hp = hp
        

# functions defined inside of a class are called methods
    def feed (self):
        print('eating')
        self.strength+= 5
        
player = Spider('Spidey', 40, 25, 75)
player.feed()
print(player.strength)
print(player.name)