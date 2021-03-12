## functions

    def function ():
        logic

    function()


# you must define your function and then include arguments in the paramenters
call your function with the name of the function and () ex: cat().

# define your variable
Something = input('type something\n')
SomethingElse = input('type something else\n')

# define your function and its arguments are passed into the parameters
def printMessage(firstMessage, secondMessage):

# define what happens when your function is ran
    combinedMessage = '\n' + firstMessage +'\n'+ secondMessage

# return data requested
    return print('this is your message: %s' % combinedMessage)

# call the functions with arguments passed for the function to run
printMessage(Something, SomethingElse)


# SCOPE
SCOPE is about having acess to certain things in your program
GLOBAL SCOPE means anyone can acess this variable function from anywhere inside your program
Local scope, or LEXICAL SCOPE, means you only have access to certain variables INSIDE of a specific place
## a local variable
only lives within the function

    c = d - global
    def function ():
        a = b - inside scope

# lists
contains stuff inside of []
    aList= [1,2, 'word']
    

# DICTIONARY
a sequence of labled values

creating requires use of {}
    dictionaryOfUsers = {'name': 'joe', 'age': '34'}

creating dictionaries with dictionaries and lists inside of them.
    users = {
        'name': 'david',
        placesLived: {
            "us": {'city': 'los angeles'}
            "space": {'location': 'clouds'}
        },
        "favorite foods": {
            'pizza': {
                'specialty':['meat lover', 'veggie', 'cheeseburger']
                'normally':'all cheese'

            }
        }
    }

# list loops
you can se len to find the length of a list

loop over a list
    while < # len():

use index to specific index position start and use
    index = 0
    while < # len():
        variable = variable[index]
        index += 1

# for loop
write te singular of the list you are looping over  
    for (singular variable) in (variable)

# combining lists
combinedList = list1 + list2
combinedList2 = list.extend([listed items])

# modify list
list[index#] = 'variable'