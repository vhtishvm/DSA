'''Binary Search: Works only on the sorted data:
My knowledge so far: Search the element from the center. Use two pointers. First, second and middle'''

a = [12,17,23,34,42,45,56,60,67,78,89,98]

l = 0
r = len(a)-1

target = 81

'''for i in range(m,r):
    if a[i] == target:
        b = True
        break
    elif a[i] > target:
        r = m-1
        m = (l+r)//2

    elif a[i] < target:
        l = m+1
        m = (l+r)//2
print(b)
print(i)

print("reached here:")'''
''

'''I did the mistake of implementing binary search with the for loop. This is stupid. For loop doesnt change its range. It runs based
on the fixed range object that has been created at the start. 

For binary search we use while loop. It checks the condition every time. '''
#Look up overflow related to r and l

found = False
while l<=r:
    m = (l+r)//2
    if a[m] == target:
        found = True
        print(f"the target is at index: {m}")
        break
    elif a[m]>target:
        r = m-1
    else:
        l = m+1

if found: 
    print("The element is found: ")
else: 
    print("element not found")


        