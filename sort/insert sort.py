def insert_sort(a):
    for i in range(1, len(a)):
        k = a[i]
        j = i
        while a[j-1] > k and j > 0:
            a[j] = a[j-1]
            j -= 1
        a[j] = k

a = [3, 2, 5, 1, 4]
insert_sort(a)
print(a)
