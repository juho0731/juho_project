# function filter(function, iterable)


def a(_list):
    c = []
    for n in _list:
        if n%2 == 1:
            c.append(n)
    return a

# 위의 함수를 filter 를 사용해서 표현하면
# 2개의 인자가 필요함 function, iterable
# founction은 요소를 선택하는 조건(True/False)를 알려줘야 함
def condition(item):
    return item % 2 == 1
result = list(filter(condition, range(1, 11)))
print(result)

# 위에서 함수 선언 대신 lambda 표현식을 사용하면?
result = list(filter(lambda x: x % 2 == 1, range(1,11)))
print(result)