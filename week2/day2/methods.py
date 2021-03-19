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
        

    def train (self):
        print('training')
        self.defense += 5

    def status (self):
        print('how are you?')
        print(petSpider)

    def stare (self):
        print('staring')
        self.hp += 5




# spidey = Spider('spidey', 20, 10, 100)
# print(spidey.strength)
# spidey.feed()
# print(spidey.strength)

def welcomeMessage():
    message = int(input('''
    1. feed 
    2. train 
    3. status
    4. stare
    5. quit
    '''))
    
    return message
    



def playerSelect ():
    print('please pick a character')
    player = ''
    
    player1 = input('')
    
    
    if player1 == 'spidey':
        player = Spider('Spidey', 40, 25, 75)
        print('youve chosen:'+ player.name)
    if player1 == 'Venom':
        player = Spider('Venom', 20, 50, 100)
        print('youve chosen:'+ player.name)
    if player1 == 'SpiderWoman':
        player = Spider('Spiderwoman', 30 , 100, 50)
        print('youve chosen:'+ player.name)
    
    # print(player.name + 'is not named %s' %(player1))
    return player
       

player = playerSelect()

choice = ''
while choice != 5:
    choice = welcomeMessage()
    if choice == 1:        
        player.feed()
        print(player.strength)
    if choice == 2:
        train()
        print(petSpider)
    if choice == 3:
        status()
        print(petSpider)
    if choice == 4:
        stare()
        print(petSpider)
    if choice == 5:
        break
    else:
        pass