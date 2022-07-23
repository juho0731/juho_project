# map(function, iterable), ...)

# range(1, 11)을 각각 항목을 문자열로 변환한 리스트 생성?
def get_str(_list):
    str_list = []
    for n in _list:
        str_list.append(str(n))
    return str_list


# 위에 함수를 map으로 활용하여 표현하면?
# 각각의 시퀀스 요소를 함수를 적용하여 새 시퀀스로 리턴
result = list(map(lambda x: str(x), range(1, 11)))
print(result)

# 입력(input) 에서의 활용법
_input = input("공백으로 구분하여 수 입력:")
result = list(map(int, _input.split()))
print(result)

# 두 시퀀스의 값을 서로 곱한 새로운 리스트
# map 은 iterable 요소를 두 개 이상 받을 수 있다.
result = list(map(lambda x, y: x*y,
                  range(1, 11), range(1, 11)))
# *** 두 시퀀스의 길이가 다르다면 짧은 시퀀스의 길이까지만 실행됨
print(result)