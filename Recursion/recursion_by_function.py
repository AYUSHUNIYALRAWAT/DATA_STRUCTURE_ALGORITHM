#Print anirudh 4 times
count = 0
def func():
    global count
    if count == 4:
        return
    print("anurudh")
    count += 1
    func()

func()


#print 1 to n 
count = 0
def func():
    global count 
    if count == 10:
       return
    print(count)
    count += 1
    func()

func()    