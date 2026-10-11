#recursive APPROACH
n=int(input("ENTER THE NUMBER : "))
    
while n >0:
    digit = n %10
    print(digit)
    n =  n//10


# BY USING STRING 
n = int(input("ENTER THE NUMBER : "))
for digit in str(n):
    print(digit)

#MATHEMATICAL APPROACH
