import random

n = [12,23,34,45,56]
s = []

for items in n:
    s.append(items*items)


print(s)

#Finally learnt list comprehension
x = [x*2 for x in range(6)]
print(x)

#Create a list of numbers from 1–10 but add +1 to each number
y = [a+1 for a in range(1,11)]

print(y)

t = []

u = [t.append(v+random.random()) for v in range(15)]
print(u)