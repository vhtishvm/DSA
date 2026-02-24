#E. Bubble Sort Trace

size = int(input())
array = list(map(int, input().split()))

for i in range(len(array)-1):
    sw = 0
    for j in range(len(array)-1-i):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1],array[j]
            sw +=1
        

    print(f"Pass {i+1}: {' '.join(map(str,array))} , swaps = {sw}")
    if sw == 0:
        break
    

