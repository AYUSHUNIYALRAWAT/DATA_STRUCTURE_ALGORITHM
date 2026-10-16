#n = list(map(int,input("ENTER THE NUMBER SEPRATE THEM WITH SPACE: ").split()))
n = [1,2,3,1,4,5,2,1,5,6,3,3,7,5,8,7,8,9,9,9,10]
m = [1,10,2,111,2,6,5,29,7,5,3]
for num in n :
    count =0
    for x in n :
       if x == num :
        count += 1
    print(num ,count)

#now better approach
n = [1,2,3,1,4,5,2,1,5,6,3,3,7,5,8,7,8,9,9,9,10]
m = [1,10,2,111,2,6,5,29,7,5,3]
hash_list = [0] * 11
for num in n :
   hash_list[num] += 1
   for num in m :
      if num < 1 or num >10:
         print(0)
      else : 
         print(hash_list[num])


