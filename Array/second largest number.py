
#second largest number
list = [10, 50, 30, 40, 20]
largest=0
second_largest=0
for num in list:
    if num > largest:
        second_largest = largest  
        largest = num             
    elif num > second_largest:
        second_largest = num  
print(largest)
print(second_largest)
