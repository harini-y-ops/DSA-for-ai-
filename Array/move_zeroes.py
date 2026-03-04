
# Move all zeros to the end!
list = [0, 1, 0, 3, 12]
new_list=[]
for num in list:
    if num>0:
        new_list.append(num)
print(new_list)
zeroes=list.count(0)
for i in range(zeroes):
    new_list.append(0)
print(new_list)
