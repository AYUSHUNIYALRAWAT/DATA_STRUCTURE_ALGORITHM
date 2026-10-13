#counting frequency 
n = [10,20,30,40,10,20,40,50,50,50,70,70,70]

frequency ={}
for i in n :
    if i in frequency:
        frequency[i] += 1
    else :
        frequency[i] =1
        print(frequency)