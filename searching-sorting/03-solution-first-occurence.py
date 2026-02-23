# a = [1,3,5,6,8,9,9,9,9,9,12,23,34,45]
# target = 9
# a = [1,2,3,4,5,6,7]
# target = 10   # target does NOT exist

a = [1,9,9,9,9,9,9,9,9]
target = 9

l = 0
r = len(a) -1

while l<=r:
    m = (l+r)//2
    if a[m] == target:
        r = m-1
    elif a[m] < target:
        l = m+1
    else: 
        r = m-1

if l < len(a) & a[l]==target:
    print(f"the first occurence for {target} is: {l}")

else:
    print("target not found.")
