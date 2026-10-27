def selection_sort(num):
    n = len(num)
    for i in range (n):
        max_ind = i
        for j in range (i+1,n):
            if num[j] < num[max_ind]:
              max_ind = j
        num[i],num[max_ind] = num[max_ind],num[i]
    return num

num = list(map(int,input("enter the num seprate it by space :").split()))
print(selection_sort(num))





#desencing order
def selection_sort_d(num):
    n = len(num)
    for i in range(n):
        max_ind = i
        for j in range(i+1,n):
            if num[j] > num[max_ind]:
                max_ind = j
        num[i],num[max_ind] = num[max_ind],num[i]
    return num
num = list(map(int,input("enter the number and seprate them by spaces : ").split()))
print(selection_sort_d(num))