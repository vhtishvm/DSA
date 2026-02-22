a = [10,7,6,4,3,2,11,9,15,17,28]

target = 9 
for x in a:
    if x == target:
        print(f"{target} is at index {a.index(x)}")
        break


#enumerate returns something like [(0,10),(1,70)]: Basically index and value both
for i,v in enumerate(a):
    if v == target:
        print(i)
