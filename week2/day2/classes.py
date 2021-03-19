class Spider:
    def __init__(self, name, strength, defense, hp):
        self.name = name
        self.strength = strength
        self.defense = defense
        self.hp = hp
    pass

#dot notation
spidey = Spider('spidey', 20, 10, 100)
print(spidey.name)
print(spidey.strength)
venom = Spider('venom', 40, 50, 200)
print(venom.name)
print(venom.strength)
carnage = Spider('carnage', 100, 100, 400)
print(carnage.name)
print(carnage.strength)

petSpider = {
    'name': 'spidey',
    'strength': 20,
    'defense': 10,
    'hp':100
}

petSpider2 = {
    'name': 'venom',
    'strength': 40,
    'defense': 50,
    'hp':200
}

#feed the spider increase his strengthegnth
def feedSpidey ():
    petSpider['strength']+= 5

# train the spider increase his defense
def trainSpidey ():
    petSpider['defense'] += 5



def spideyStatus ():
    print(petSpider)

def stare ():
    petSpider['hp'] += 5
    
   

def welcomeMessage():
    message = int(input('''
    1. feed Spidey
    2. train Spidey
    3. Spidey status
    4. stare
    5. quit
    '''))
    
    return message
    

choice = ''
while choice != 5:
    choice = welcomeMessage()
    if choice == 1:
        feedSpidey()
        print(petSpider)
    if choice == 2:
        trainSpidey()
        print(petSpider)
    if choice == 3:
        spideyStatus()
        print(petSpider)
    if choice == 4:
        stare()
        print(petSpider)
    if choice == 5:
        break
    else:
        pass