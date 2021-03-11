while(True):

    def multiply (number1, number2):
        return number1*number2

    def divide (number1, number2):
        return number1/number2

    def add (number1, number2):
        return number1+number2

    def subtract (number1, number2):
        return number1-number2
    def stop (operator):
            print('end')
        
    

    operator = input('pick an operator: *, /, +, -')
    number1 = int(input('pick a number'))
    number2 = int(input('pick a 2nd number'))

    if operator == '*':
        print(multiply(number1, number2))
    if operator == '/':
        print(multiply(number1, number2))
    if operator == '+':
        print(multiply(number1, number2))
    if operator == '-':
        print(multiply(number1, number2))
  
    

