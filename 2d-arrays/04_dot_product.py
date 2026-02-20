

def dot(v1,v2):
    a = 0
    for i in range (len(v1)):
        a += v1[i]*v2[i]
    return a
a = [1,2,3,4]
b = [3,4,5,6]
print(dot(a,b))
