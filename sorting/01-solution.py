'''My version of selection sort'''

# array = [12,43,23,65,34,13,16,25,2,74,78,75,43,38,5,17]
array = [1,2,3,4,5,6,7]


for i in range(len(array)):
    minimum = array[i]
    loc = i
    for j in range(i,len(array)):
        if array[j] < minimum:
            minimum = array[j]
            loc = j
    print(f"The array so far: {array}")
    array[loc] = array[i]
    array[i] = minimum

print(array)
