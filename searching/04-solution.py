size = int(input())
array = list(map(int, input().split()))
target = int(input())

flag = False
for x in array:
    if x == target:
        flag = True

if flag:
    print("YES")
else:
    print("NO")

