#by using recursion 
n = int(input("ENTER THE NUMBER: " ))
num = n
result = 0
while num > 0 :
    last_digit = num % 10
    result = (result * 10) + last_digit
    num = num // 10
if ( n == result):
    print("the number is palindrome")
else :
    print("the number is not palindrome")


# by using string
n =input("Enter the number : ")
if n ==n[::-1]:
    print("It is palindrome")
else : 
    print("It is not palindrome")


#
