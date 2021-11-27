import random
a = []
for i in range(5):
     random_num = random.randrange(1,200)
     a.append(random_num)
print(a)
for k in range(len(a)):
     min = k
     for i in range(k,len(a)):
          if a[min] > a[i]:
               min = i
          a[k],a[min] = a[min],a[k]
print(a)
