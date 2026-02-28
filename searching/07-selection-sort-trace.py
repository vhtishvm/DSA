size = int(input())
array = list(map(int,input().split()))

for i in range(len(array)-1):
    minimum = array[i]
    r = i


    for j in range(i,len(array)):
        if array[j] < minimum:
            minimum = array[j]
            r = j

    array[r] = array[i]
    array[i] = minimum
    
    print(f"Pass {i+1}: {' '.join(map(str,array))} , min_selected = {minimum}")

