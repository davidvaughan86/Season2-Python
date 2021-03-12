# string1 = input('find how many words there are\n')


# def exampleCalc(word):
#     length = len(word)
#     print('======')
#     return print(length)
# exampleCalc(string1)

typeSomething = input('type something\n')
typeSomethingElse = input('type something else\n')

def printMessage(firstMessage, secondMessage):
    combinedMessage = '\n' + firstMessage +'\n'+ secondMessage
    return print('this is your message: %s' % combinedMessage)

printMessage(typeSomething, typeSomethingElse)