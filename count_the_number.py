
n=int(input("ENTER THE NUMBER : "))

count = 0
while n >0:
        n = n//10
        count = count +  1
print("Number of digits: ",count)

#by using string
num =12345
print(len(str(num)))

#mathematical approach
import math
n = int(input("ENTER THE NUMBER : "))
digits = int(math.log10(n)) + 1
print(digits)