n = [12,23,34,45,56]
s = []

for items in n:
    s.append(items*items)


print(s)

#Finally learnt list comprehension
x = [x*2 for x in range(6)]
print(x)