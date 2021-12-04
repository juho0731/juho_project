import random
a = []
def make_random_list():
    for i in range(10):
        a.append(random.randrange(1, 11))
    return a
temp_list = make_random_list()
print()

def find_max_value(a):
    max_value = a[0]
    for i in range(len(a)):
        if max_value < a[i]:
            max_value = a[i]
    return max_value
result = find_max_value(temp_list)
print(result)
