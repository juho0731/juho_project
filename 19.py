c = int(input())
d = list(map(int, input().split(' ')))
maximum = -1000001
minimum = 1000001
for i in range(len(d)):
    if maximum < d[i]:
        maximum = d[i]
    if minimum > d[i]:
        minimum = d[i]
print(minimum,maximum)
