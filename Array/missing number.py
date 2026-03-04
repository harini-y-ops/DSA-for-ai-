list=[1,2,3,4,6]
n=len(list)+1
expected_sum=n*(n+1)/2
actual_sum=0
for num in list:
    actual_sum+=num
missing=(expected_sum-actual_sum)
print(f"Missing number is {missing}")

