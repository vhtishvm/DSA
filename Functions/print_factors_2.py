n = int(input("Enter your number:"))

def fact(n):
    i = n
    while i>=1:
        if n%i == 0:
            print(i)
        i -=1

fact(n)
