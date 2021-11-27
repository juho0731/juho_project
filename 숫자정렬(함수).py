import random

def bubble_sort(a):
    for i in range(len(a)):
        for i in range(len(a)-1):
            if a[i]>a[i+1] :
                a[i],a[i+1] = a[i+1],a[i]
    return a
a =[]
for i in range(5):
     random_num = random.randrange(1,200)
     a.append(random_num)
print(a)
a = bubble_sort(a)
print(a)
