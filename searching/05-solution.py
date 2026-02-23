size = int(input())

array = list(map(int,input().split()))

target = int(input())

l = 0
r = size-1
flag = False
while l <= r:
    m = (l+r)//2
    if array[m] == target:
        flag = True
        break
    elif array[m] > target:
        r = m - 1
    else: 
        l = m+1

if flag: 
    print("YES")
else: 
    print("NO")