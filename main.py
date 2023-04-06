from threading import main_thread

mtList=["king","Queen","Knight",40,"Pawn","Rook","Bishop",True,84]
print(mtList)
#lists are defined as objects with the data type 'list'.
#PythonDS it a collection of object which is ordered changable and it allows duplicate.

print(len(mtList))
#printing the number of list

print(mtList[1])
print(mtList[-1])
# helps to print the item stored in 1st position on that list.
#-1 refers to the last item

print(mtList[1:3])
#printing items which are in the position 1 2 and 3.
#index not included in this case

print(mtList[:4])
#This example returns the items from the beginning to, but NOT including item in the 4th position

print(mtList[2:])
# This will return the items from index 2 to the end.

if "king" in mtList:
    print("YES")

# to check the item is there in the list or not.

mtList[3]=50
print(mtList)
#Replacing ghe first item to black queen

mtList[4:6]=["Black Pawn","Black Rook"]
print(mtList)
#Replacing the value from one position to another position

mtList.insert(2,89)
print(mtList)
# To insert an item in the list in a perticular position

mtList.append(100)
print(mtList)
# append an item to the list.

moList = ["ok","okk"]
mtList.extend(moList)
print(mtList)
#appending a list to the current PythonDS

tropical = ["mango", "pineapple", "papaya"]
mtList.extend(tropical)
print(mtList)



thistuple=("abc","bca")
mtList.extend(thistuple)
print(mtList)
# extend method does not have to append the list, it cann append tuples, sets, dictionaries.

mtList.remove("abc")
print(mtList)

for x in mtList:
    print(x)
#printing all the elements in mList.

print(mtList)
mtList.pop(11)
print(mtList)
#pop remove in the item in that perticular index
#del is also do the same.

moList.clear()
#clear is used clear the list

for i in range(len(mtList)):
    print(i)
# printing i value depend on the number of items present in list using for loop

i = 0
while i < len(mtList):
    print(mtList[i])
    i = i + 1
#using while loop

newList=[]
for x in mtList:
    if "a" in x:
        newList.append(x)

print(newList)

#List comprehension gives a shorter syntax when you want to create a new list based on the values of an exsisting list.

