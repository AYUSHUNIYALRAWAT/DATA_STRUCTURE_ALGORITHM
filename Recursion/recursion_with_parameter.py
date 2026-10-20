#rrecursion using parameter
#print x ,n times
'''N = int(input("Enter the number: "))

def func(x, N):
    if N <= 0:
        return
    print(x)
    func(x, N - 1)

func("ayush", N)

#print 1 to N

def func(i,n):
    if i > n:
        return
    print(i)
    func(i+1,n)

i = int(input("Enter the number : "))
n = int(input("Enter the number : "))
func(i,n)'''


#print 1 to n by using tail recursion with parameter
def func(i,n):
    if i > n :
        return 
    func(i+1,n)
    print(i)

i = int(input("Enter the number : "))
n = int(input("Enter the number : "))
func(i,n)
