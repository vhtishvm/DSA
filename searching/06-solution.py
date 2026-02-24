size = int(input())
array = []

for i in range(size):
    array.append(input())

name  = input()

flag = False
l = 0 
r = len(array) - 1

while l<=r:
    m = (l+r)//2

    if array[m] == name:
        flag = True
        break
    elif array[m] > name:
        r = m-1
    
    else: 
        l = m+1

if flag: 
    print("YES")
else: 
    print("NO")



