 #remove all negative numbers 
list = [1, -2, 3, -4, 5, -6, 7]
new_list=[]
for num in list:
    if num>0:
        new_list.append(num)
print(new_list)
