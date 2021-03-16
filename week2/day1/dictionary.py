dcStudent = {
    'name': '',
    'age': '',
    'city': '',
    'computer':[]
}

game = {
    'platform': '',
    'gaminghours': [{'weekdays':'9-5', 'weekend':'anytime'}],
    'skill': ''
}

car = {
    'model': '',
    'image': [],
    'year': '',
    'engineChoices': [{
        'v4': {
            'horsepower':250
        },
        'v6': {
            'horsepower':350
        },
        'v8': {
            'horsepower':450
        },
        'v10': {
            'horsepower':550
        },
        'v12': {
            'horsepower':650
        }
    }]
}


# 2. print out the horsepower values only (all of them)




# 1. print out a list of engine choices (the whole list)
print(car)
# 2. print out the horsepower values only (all of them)
print(car['engineChoices'])
for hpValue in car['engineChoices']:
    for key,value in hpValue.items():
        print(value['horsepower'])

# 3. check to see if the key "trim" exist on the car dictionary


# 4. add a new key to the car dictionary called "colors" which will be a list of all possible colors (use 4 color strings)
car.update({'colors': ['black','gold','silver','red']})
print(car)

# # 5. find an image and put the url into https://bitly.com/, and paste shortened url into that "image" value
car['image'].append('https://bitly.com/')
print(car)

