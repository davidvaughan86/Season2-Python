nameOfUser = input('what is your name?\n')
print('==================')
# stores the user first name in a number value that can be used
lengthOfUserName = len(nameOfUser)

# if statement

# if lengthOfUserName > 0:
#     print('please enter a valid username')
# else:
#     print('please enter at least one letter')
#while():

# while loop

while(lengthOfUserName < 4):
    nameOfUser = input('what is your name?\n')
     # we must reassign the value of lenthofusername to check the while loop
    lengthOfUserName = len(nameOfUser)
    print('==================')
   
    

lastNameOfUser = input('what is your last name?\n')
# stores the user last name in a number value that can be used
lengthOfUserLastName = len(lastNameOfUser)
print('==================')


while(lengthOfUserLastName < 4):
    lastNameOfUser = input('what is your last name?\n')
     # we must reassign the value of lenthofusername to check the while loop
    lengthOfUserLastName = len(lastNameOfUser)
    print('==================')
    


print(lengthOfUserName , 'is the legnth of the user first name?' )
print('==================')
print(lengthOfUserLastName, 'is the legnth of the user last name?') 
print('==================')


print('the user name is %s %s' %(nameOfUser, lastNameOfUser))

if lengthOfUserName > 7:
    # if the statement is TRUE, returns the rest of the code in here
    print('ok its valid so one more question')
    print('==================')
    nameOfFriend = input('what is your friends name?\n')
    print('==================')
    print('your friends name is %s and your full name is %s %s' %(nameOfFriend, nameOfUser, lastNameOfUser))
else:
    print('unfortunately your name isnt long enough to have friends, good bye.')
