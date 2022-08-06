def merge_sort(a):
    if len(a) <= 1:
        return a

    mid = len(a)//2
    left_a = merge_sort(a[:mid])
    right_a = merge_sort(a[mid:])

    merged_a = []
    l = 0
    r = 0

    while l < len(left_a) and r < len(right_a):
        if left_a[l] > right_a[r]:
            merged_a.append(right_a[r])
            r += 1
        else:
            merged_a.append(left_a[l])
            l += 1
    merged_a += left_a[l:]
    merged_a += right_a[r:]

    return merged_a

a = [6, 2, 8, 1, 3, 9, 4, 5, 10, 7]
a = merge_sort(a)
print(a)


