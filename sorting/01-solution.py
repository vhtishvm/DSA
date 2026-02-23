'''My version of selection sort'''

array = [12,43,23,65,34,13,16,25,2,74,78,75,43,38,5,17]



for i in range(len(array)):
    minimum = array[i]
    r = i

    for j in range(i,len(array)):
        if minimum > array[j]:
            minimum = array[j]
            r = j
    
    array[r] = array[i]
    array[i] = minimum

print(array)