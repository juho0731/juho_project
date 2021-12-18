n = 51
m = 100

def find_prime(a):
    count = 0
    for i in range(2 , a//2+1):
        if a % i == 0:
            count += 1
            break

    if (count == 0 or a== 2) and a!= 1:
        return 1
    else:
        return 0
total_sum = 0
first_prime = 0

for i in range(n, m +1):
    flag = find_prime(i)
    if flag == 1:
        total_sum += i
        if first_prime == 0:
            first_prime = i
if first_prime == 0:
        print("-1")
else:
    print(total_sum)
    print(first_prime)
