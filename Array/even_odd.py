#Count even and odd numbers
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count=0
odd_count=0
for num in list:
    if num%2==0:
        even_count+=1
    elif num%2==1:
        odd_count+=1
print(f"The number of even numbers:{even_count}")
print(f"The number of odd numbers:{odd_count}")
