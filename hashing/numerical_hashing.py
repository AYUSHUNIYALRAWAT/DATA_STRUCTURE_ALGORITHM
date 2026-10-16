n = [1,2,3,1,4,5,2,1,5,6,3,3,7,5,8,7,8,9,9,9,10]
m = [1,10,2,111,2,6,5,29,7,5,3]
freq = {}
for num in n:
    freq[num] = freq.get(num,0)+1
for num in m:
    print(num,freq.get(num,0))