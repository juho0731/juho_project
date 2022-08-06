def bubble(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
a = [3, 2, 5, 1, 4]
bubble(a)
print(a)
