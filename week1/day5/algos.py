1.
#1. Fizz Buzz
# Write a program that prints the numbers from 1 to 100. 
# But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".

# Python program to print Fizz Buzz
 
# Loop for 100 times i.e. range
for fizzbuzz in range(101): 
    
    # Number divisible by 15,(divisible 
    # by both 3 & 5), print 'FizzBuzz' 
    # in place of the number
    if fizzbuzz % 15 == 0: 
        print("FizzBuzz")                                         
        continue
 
    # Number divisible by 3, print 'Fizz'
    # in place of the number
    elif fizzbuzz % 3 == 0:     
        print("Fizz")                                         
        continue
 
    # Number divisible by 5, 
    # print 'Buzz' in
    # place of the number
    elif fizzbuzz % 5 == 0:         
        print("Buzz")                                     
        continue
 
    # Print numbers
    print(fizzbuzz)

2.
#Sum of All Multiples of 3 or 5 below 1000
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


# Python3 program to find the sum of  
# all multiples of 2 and 5 below N  
  
# Function to find sum of AP series  
total = 0
for num in range(1000)
    if num % 3 == 0 or num % 5 == 0:
        total = total + num
    print(num)

3.

odd, even = 0, 1
total = 0
while True:
    odd, even = even, odd + even
    if even >= 4000000:
        break
    if even % 2 == 0:
        total += even
print(total)
