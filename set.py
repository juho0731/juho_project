# class set([iterable})
# 참수가 아닌 형식.
# 입력 받은 iterable 객체를 set 으로 변환.

print(set([1,2,2,3])) # 리스트를 집합으로 변환
print(set((1,2,2,3))) # 튜플을 집합으로 변환
print(set(range(4)))  # range 스퀀스를 집합으로 변환
print(set({"1": 1, "2": 2})) # 딕셔너리를 집합으로 변환