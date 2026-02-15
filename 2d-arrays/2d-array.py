#Pattern printing
n = 5 
m = 5

for i in range(5):
    for j in range(5):
        if (i+j)%2 == 0:
            print(0,end="")
        else:
            print(1,end="")
    print("")
