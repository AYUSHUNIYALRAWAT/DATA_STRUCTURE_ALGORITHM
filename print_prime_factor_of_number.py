#print prime factor
n = int(input("enter the number :"))
result=[]
for i in range(1,n+1):
    if n % i ==0:
        result.append(i)
        print(result)



# This is better approach
n = float(input("ENTER THE number :"))
result=[]
for i in range(1,n/2 +1):
    if n % i ==0:
        result.append(i)
        print(result)


#This is optimal solution
from math import isqrt

num = int(input("Enter The Number: "))

if num <= 0:
    print("Please enter a positive integer.")
else:
    result = []
    for i in range(1, isqrt(num) + 1):
        if num % i == 0:
            result.append(i)
            if num // i != i:
                result.append(num // i)

    result.sort()
    print(result)
