
count = 0
d = int(input())
for i in range(2, d):
    if d % i == 0:
       count += 1
if count == 0:
    print("prime")
else:
    print("Not prime")
