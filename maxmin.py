#max(iterable *[, key, default])
#max(arg1, arrg2, *arrgs [,key]
# min 도 위와 동일
#1. 입력받은 iterable(반복가능) 객체 중 제일 큰 값 리턴
#2. 입력받은 인자값 중 제일 큰 값 리턴
# - min 은 위의 반대

# print(max([1, 3, 4]))     # 4
# print(max(1,2,"4"))       #TypeError
#c print(max(3))             # TypeError
# print(max([]))            #ValueError
# print(max([], default=0)) # 0
# # print(max([1,9], [4, 7])) # [4, 7]
# print(max([1, 9], [4, 7],
#           key=lambda x: x[1])) # [1, 9]
# print(max([1, 9], [4, 7],
#           key=lambda x: sum(x))) # [4, 7]
# print(max("absdefg")) # g
# print(max("a", "A")) # a