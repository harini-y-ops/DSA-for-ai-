#Rotate a list by one position to the right
list=[1, 2, 3, 4, 9]
last=list.pop()
list.insert(0,last)
print(list)
