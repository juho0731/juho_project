import random

a =[]
for i in range(5):
    a.append(random.randrange(1,100))
print(a)
for i in range(5):
    for i in range(4):
        if a[i]>a[i+1] :
            a[i],a[i+1] = a[i+1],a[i]
print(a)

