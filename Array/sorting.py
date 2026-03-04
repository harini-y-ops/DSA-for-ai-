list = [1, 2, 3, 4, 5] 
is_sorted=True 
for i in range(len(list)-1):
    if list[i]<list[i+1]:
        is_sorted=True
       
    else:
        is_sorted=False
if is_sorted:
    print("It is sorted")
else:
    print("It is not sorted")
