# Head recursion

# print name N times
'''count = 0
def func():
    global count
    if count > 10:
        return
    count +=1
    print("anirudh")
    func()

func()    

#print number from n to 1 using recursion
count = int(input("Enter the number : "))
def func():
    global count 
    if count == 0:
        return
    count -= 1
    print(count)
    func()

func()
'''
# Tail Recursion 
#print name n times
count = 0 
def func():
    global count
    if count == 10:
        return 
    count += 1
    func()
    print("anirudh")

func()



#print number n to 1 
count = int(input("enter the number : "))
def func():
    global count 
    if count == 0:
        return 
    count -= 1
    current = count
    func()
    print(current)

func()   


    