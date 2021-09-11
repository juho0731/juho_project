#1 ~ 5 random value total 100in list

import random
a = []
b = 0
c = 0
e = 0
f = 0
g = 0
for i in range(0, 99):
    a.append(random.randrange(1, 6))
print(a)
for j in range(0, 99):
    if 1 == a[j]:
        b = b + 1
    if 2 == a[j]:
        c = c + 1
    if 3 == a[j]:
        e = e + 1
    if 4 == a[j]:
        f = f + 1
    if 1 == a[j]:
        g = g + 1
print(b, c, e, f, g)
