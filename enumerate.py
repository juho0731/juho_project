# enumerat(iterable, start=0)
# 입력받은 iterable 객체의 요소와 그 순서 변호를 strat 부터 짝지은
# 새로운 시퀀스를 리턴

a = ['a', 'b', 'c', 'd', 'e']

result = list(enumerate(a)) #start 는 0부터 출발
print(result)

# zip 으로도 흉내 가능
result = list(zip(range(len(a)), a))
print(result)

result = list(enumerate(a, start=3)) # start 는 3부터 출발
print(result)

