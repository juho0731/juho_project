def quick(a, left, right):
    if right - left <1:
        return
    p = a[(left + right)//2]
    i = left
    j = right
    while i < j:        #left, right가 만나거나 교차하기 전까지 반복
        while a[i] < p: # pivot보다 큰 a[i]를 찾음
            i += 1
        while a[j] > p: # pivot보다 작은 a[i]를 찾음
            j -= 1
        a[i], a[j] = a[j], a[i]

    quick(a, left, i-1)
    quick(a, j + 1, right)

a = [3, 9, 2, 8, 5, 1, 6, 4, 7]
quick(a, 0, len(a)-1)
print(a)




