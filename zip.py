# zip(*iterable, strict=False
# 두 개 이상의 iterable 객체의 요소들을 짝지어준 새로운 시퀀스를 리턴

a = ['one', 'two', 'three', 'four']
b = [1, 2, 3, 4, 5, 6, 7, 8]

result = list(zip(a, b))
print(result)

# *** strict=True 인 경우 엄격 모드
result = zip(a, b, strict=True)
print(list(result))