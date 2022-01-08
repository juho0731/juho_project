# a = int(input("수학:"))
# b = int(input("과학:"))
# c = int(input("국어:"))
# print((a+b+c)/3)

# 자료형
#
# 숫자
# 정수
# 실수

# 문자열
# 문자열의 연산
# 덧셈 = 문자열 붙이기
# 곱셈 = 문자열 반복
# 인덱싱
# 슬라이싱 a[n:m:o], n = 시작, m = 끝, o = 오프셋
#a = 'life is too short.'
#print(a[:4])
#(a[::-1])문자를 뒤집을 때
#포맷팅(format) = 문자열
#print("I am %d years old" %6)
#print(정수 = %d, 실수 =%f, 8진수 = %o, 16진수 = %x, 문자열 = %s)%(1,1.0. 8,16,'31241423')
# number = "881120-1068234"
# year = number[:2]
# month = number[2:4]
# day = number[4:6]
# gender = number[7]
#
# if gender in ['1', '2']:
#     year = '19' + year
# else:
#     year = '20' + year
# if gender in ['1','3']
#     gender = '남자'
# else:
#     gender = '여자'
# print('%s년 %s월 %s일 성별:%s'%(year, month, day, gender))

#list
#덧셈 = 리스트 붙이기
#곱셈 = 리스트의 내용 반복
#값추가 = append, insert
#값제거 = delete, pop, remove
#확장 = extend == 리스트 덧셈
# a =[1, 2, 3, 4, 5]
# a.sort(reverse=True) , b = sorted(a, reverse = True)
# print(a) , print(b)

# a =[1, 2, 3, 4, 5]
# a.inserrt(2, 'hello')
# print(a)

#갯수 세기 = len, count
# a =[1, 2, 3, 4, 5, 5, 5]
#print(len(a), a.count(5))

#튜플(값을 변경할 수 없는 리스트)
# t1 = ()       #비어있는 튜플
# t2 = (1)      #값이 하나 있는 튜플
# t3 = (1, 2)   #값이 두개 이상 있는 튜플
# t4 = 1,2,3    #값이 두개 이상이면 괄호 생략
#인덱싱 , 슬라이싱 가능
#덧셈, 곱셈가능
# t = 1, 2
# t = t +(3,4)
# print(t)

#딕셔너리(dictionary)
# 값을 조회 할때 = d[key]
# print (d[True])
# 값을 변경 할때 = d[key]= value
# d[3] = 'three'
# print(d[3])
# 값을 추가가 할때 = d[new_key]=value
# d['new'] = 'new value'
# 값을 삭제 할때 = del d[key]
# del d[(1, 2)]
# print(d)
#
# d = {1 :'v', 'h': 3, 3.0 : '4'}

#key리스트 만들기 = list.(d.keys())
#value리스트 만들기 = list.(d.values())
#key,value 쌍 리스트 만들기 = list(d.items())

#집합(set)
#set
#합집합(union),차집합(difference), 교집합(intersection)
#순서가 없다, 중복이 없다.
# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# s3 = union(s2)
# print(s3)
#리스트에서 중복을 제거하고 오름차순으로 정렬하세요
# a = [3, 2, 1, 3, 4, 6, 7, 6, 6, 7]
# b = list(set(a))
# b.sort()
# print(b)

#불(bool)
#단 두가의 값만 가진다.True or False
#a = 1
#a = 2
#print(a== b)
#print(a != b)
#print(a > b)
#print(a < b)
#print(a < b and a != b)
#print(a > b or a== b)
#print(1 in [1, 2, 3]
#print(1 not in [1, 2, 3]
#print(not(1 in [1, 2, 3]))