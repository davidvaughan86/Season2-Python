# python week 2

# Dictionaries vs Lists

aDict = {}

aList= []

a list can have 3 types

['a', 1, True]

key pair values in a dictionary

aDict = {'key':'value'}

key pair values can be 3 types

{'key': 'a'}
{'key': 1}
{'key': True}

# nested dictionaries

a list in a dictionary
aDict = {'a':[1,2,3]}

a dictionary in a dictionary
aDict = {'a':{'b': 1}}

a list in a dictionary in a dictionary
aDict = {'a':{'b': [1,2,3]}}

# printing values

list1 = ['string', 17, True]

dict1 = {
    '1': 'a',
    '2': 'b',
    '3': [
        '1', '2', '3'
    ],
    '4':{'v': [
        'x','y','z'
    ]}
}

print(dict1) returns the entire dictionary
print(list1) returns the entire list
print(list1[1]) returns position 1 of list index
print(dict1['3']) returns dictionary 3's list
print(dict1['3'][0]) returns the index 0 position of the list of key 3
print(dict1['4']) returns dictionary 4's dictionary list
print(dict1['4']['v']) returns the 'v' dictionary list in the dictionary of '4'
print(dict1['5'][0]) returns the index 0 (n:0) position of the list of dictionary key (5)
print(dict1['5'][0]['n']) prints the value (o) of the dictionary (n) in the list of the dictionary of (5)