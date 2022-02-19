def Binary_search(l, target):
    left = 0
    right = len(l)-1

    while right >= left:
        mid = (left + right)//2
        if target == l[mid]:
            return 1

        if target > l[mid]:
            left = mid+1

        elif target < l[mid]:
            right = mid-1
    return 0

n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
b = list(map(int,input().split()))
for i in b:
    print(Binary_search(a,i))
