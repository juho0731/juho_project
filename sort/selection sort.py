def selection_sort(a):
    for i in range(len(a)):
        k = i
        for j in range(i+1, len(a)):
            if a[k] > a[j]:
                k = j
        a[k], a[i] = a[i], a[k]

a = [3, 2, 5, 1, 4]
selection_sort(a)
print(a)
