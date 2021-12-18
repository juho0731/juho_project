b = []
A = int(input())
B = int(input())
C = int(input())
a = str(A*B*C)
print(a)
count_list=[0,0,0,0,0,0,0,0,0,0]
for i in range(len(a)):
    b.append((a[(len(a)-1)-i]))
for i in range(len(b)):
    num = int(a[i])
    count_list[num] += 1
print(count_list)