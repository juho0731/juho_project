
import random

e = []
for i in range(10):
    e.append (random.randrange(1, 100))
print(e)

max_value = e[0]
for i in range(len(e)):

    if max_value> e[i]:
        max_value = e[i]

