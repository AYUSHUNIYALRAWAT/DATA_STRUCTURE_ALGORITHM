#by using armstrong
n = int(input("Enter the number :"))
num = n
total = 0 
nod = len(str(n))
while n > 0:
    last_digit = n % 10
    total = total + (last_digit ** nod)
    n = n//10
if num == total:
    print("The number is armstrong ",num ,total)
else :
    print("The number is not armstrong")