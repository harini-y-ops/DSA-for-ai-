
#Find all pairs that add up to a target number
list = [1, 2, 3, 4, 5, 6]
target = 7
for i in range(6):
    for j in  range (i+1,6):
        if list[i]+list[j]==7:
            print(f"{list[i]},{list[j]}")
