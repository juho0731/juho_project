
for i in range(1, 11):
  print((11-i)*"*")
#소수
count = 0
d = int(input())
for i in range(2, d):
    if d % i == 0:
       count += 1
if count == 0:
    print("prime")
else:
    print("Not prime")
#랜덤한 값10개
import random

e = []
for i in range(10):
    e.append (random.randrange(1, 100))
print(e)

max_value = e[0]
for i in range(len(e)):

    if max_value> e[i]:
        max_value = e[i]





)