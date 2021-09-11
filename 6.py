
import random
a = []

for i in range(100):
    b = random.randrange(1,6)
    a.append(b)

count_list = [0,0,0,0,0]
for i in range(len(a)):
    num = a[i] - 1
    count_list [num] += 1
print(count_list)