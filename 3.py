#login하기
c = []
d = []
for i in range(5):
    a = input("id")
    b = input("psw")
    count = 0
    for i in range(len(c)):
        if c[i] == a:
            count  = 1
    if count == 1:
        print("over lap")
    else:
        c.append(a)
        d.append(b)
print(c,d)
