# class tuple([iterable])
# 함수가 아닌 형식.
# 입력 받은 iterable 객체를 tuple 로 변환.
# tuple은 immutable한(불변) 객체

print(tuple([1, 2, 3])) # 리스트를 튜플로
print(tuple({1, 2, 3})) # 집합을 튜플로
print(tuple({"1": 1, "2": 2})) # 딕셔너리를 튜플로
print(tuple(range(4))) # range 스퀀스를 튜플로