print('------------------------')
number1 = input('pick a number\n')
firstNumber = len(number1)
print('------------------------')

while firstNumber < 0:
    number1 = input('pick a number\n')
    firstNumber = len(number1)
    print('------------------------')


number2 = input('pick another number\n')
secondNumber = len(number2)
print('------------------------')

while firstNumber < 0:
    number2 = input('pick a number\n')
    secondNumber = len(number2)
    print('------------------------')


math = input(['add' , 'subtrat' , 'divide' , 'multiply >>>'])


if math == 'add':
    result = int(number1)+int(number2)
    print(result)
elif math == 'subtract':
    result = int(number1)-int(number2)
    print(result)
elif math == 'divide':
    result = int(number1)/int(number2)
    print(result)
elif math == 'multiply':
    result = int(number1)*int(number2)
    print(result)
else:
    print('you did not pick any math')
