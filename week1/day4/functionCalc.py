
def multiply (number1, number2):
    return int(number1)*int(number2)

def divide (number1, number2):
    return int(number1)/int(number2)

def add (number1, number2):
    return int(number1)+int(number2)

def subtract (number1, number2):
    return int(number1)-int(number2)
history = []
selection = []
while True:
    print('CALCULATOR TIME!!!!')
    print('---------------')
    number1 = input('pick a number\n')
    print('---------------')
    if number1 == 'stop':
        break
    if number1 == 'history':
        print(history)
        break
    operator = input('pick an operator: *, /, +, -, stop\n')
    print('---------------')


    number2 = input('pick a 2nd number\n')
    print('---------------')
    print('thinking finished in 0.0000010 ms')

    selection.append(number1)
    selection.append(operator)
    selection.append(number2)
    print(selection)


    if operator == '*':
        answer = multiply(number1, number2)
        print('---------------')
        print('the answer is %s' % answer)
    if operator == '/':
        answer = divide(number1, number2)
        print('---------------')
        print('the answer is %s' % answer)
    if operator == '+':
        answer = add(number1, number2)
        print('---------------')
        print('the answer is %s' % answer)
    if operator == '-':
        answer = subtract(number1, number2)
        print('---------------')
        print('the answer is %s' % answer)
    
    history.append(answer)
    


