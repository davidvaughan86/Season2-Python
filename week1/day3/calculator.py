# In this assignment you are going to build a calculator. You are going to take three inputs from the user.

# Input 1 - Represents the first number

# Input 2 - Represents the operand (+, - , * , /)

# Input 3 - Represents the second number

# Based on the operand you are going to perform the math operation and print the result on the terminal.

# Make sure each math operation is a separate function.

print('------------------------')
number1 = input('pick a number\n')
firstNumber = len(number1)
print('------------------------')

while firstNumber < 0:
    number1 = input('pick a number\n')
    firstNumber = len(number1)
    print('------------------------')



math = input('pick an operand ( *, /, -, + )\n')
print('------------------------')



number2 = input('pick another number\n')
secondNumber = len(number2)
print('------------------------')

while secondNumber < 0:
    number2 = input('pick a number\n')
    secondNumber = len(number2)
    print('------------------------')

if math == '*':
    result = int(number1)*int(number2)
    print('the answer is:')
    print('>%s<' % result)
elif math == '/':
    result = int(number1)/int(number2)
    print('the answer is:')
    print('>%s<' % result)
elif math == '-':
    result = int(number1)-int(number2)
    print('the answer is:')
    print('>%s<' % result)
elif math == '+':
    result = int(number1)+int(number2)
    print('the answer is:')
    print('>%s<' % result)
else:
    print('looks like you didnt choose an operand')
    



