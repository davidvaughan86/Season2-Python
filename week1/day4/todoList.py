#  start the list 

#  add to the list
#  determine priority of the list item

#  view the list

#  delete the items on the list

#  stop the list


aList = []
print(aList)
def message():
    print('welcome to the todo list')

message()

def addItem ():
    print('please add your item')
    newItem = input(str(''))
    newItemlen = len(newItem)
    while newItemlen < 3:
        print('please add a valid number of characters for your item (3)')
        newItemlen = len(newItem)
    if newItemlen >= 3:
        aList.append(newItem)
        print('this whas just added' + newItem)
        print(aList)
def viewItem():
    print(aList)
    # print(aList[1])
    # i = aList.index(i)
    # print(i)


def delItem():
    print(aList)
    i = 0
    for list in aList:
        i = i + 1
        print(i, list)
    print('Select (#) to delete from list. Press (b) to return to menu')
    deletedItem = input(str(''))
    if deletedItem == 'b':
        message()
    if deletedItem == '1':
        del aList[0]
        print(aList)
    if deletedItem == '2':
        del aList[1]
        print(aList)
    if deletedItem == '3':
        del aList[2]
        print(aList)
    if deletedItem == '4':
        del aList[3]
        print(aList)
    if deletedItem == '5':
        del aList[4]
        print(aList)
       







while True:
    choice = input({
         '1': 'Add item to list',
         '2': 'View items on list',
         '3': 'Delete items from list'
     })
    if choice == 'q':
        print('exiting')
        break
            
    else:
        message()

    if choice == '1':
        addItem()
   
    if choice == '2':
        viewItem()

    if choice == '3':
        delItem()
   
   