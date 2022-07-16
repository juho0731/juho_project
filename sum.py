#sum(iterable, start=0)
# iterable 항목들을 왼쪽에서 오른쪽으로 합하고 합계를 리턴한다.
# start 값은 시작값을 넘길 수 있다.(시작값은 문자열이 될 수 없다.)

# print(sum([1,2,3]))  #6
# print(sum((1,2,3)))  #6
# print(sum(range(4))) #6
# print(sum([1,2,3], start=6)) # 12
# print(sum(["1","2","3"])) # TypeError
# print(''.join(["1", "2", "3"])) # 123
