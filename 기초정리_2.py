# 1. 반복되는 내용을 재사용하기 위해서 작성
# 2.어떠한 입력에 대한 출력을 정의
# def 함수명(매개변수)
# <수행할 문장>
# <수행 할 문장>,,,
#3. 매개변수가 여러개 일때는? (*매개변수)
#4. 키워드 매개변수(**매개변수)
#5.결과값(return)은 항상 하나다.
#6. 매개변수에는 초기값을 지정할 수 있다.
#7. 변수의 범위(scope)는 함수 내에서만 유효하다.
#8. 함수 밖의 변수를 함수 내에서 변경 가능하다.(global)
#9. 한줄 짜리 함수 작성 가능(lambda)
#10.함수는 자기 자신을 호출할 수 있다.(재귀(recursive)함수 라고 함)
#재귀 함수는 일반항을 구하는 것이 중요! s(N) =s(N-1) + N
# def my_sum(n):
#     s = 0
#     for i in range(1, n+1):
#         s += i
#     return s
#
#
# def add(a, b):
#     return a + b
# add2= lambda a, b: a+b
#
# print(add(1,3))
# print(add2(1,3))

# def people(name, age, gender='남성'):
#    print(f'이름은{name}, 나이는 {age}살, 성별은 {gender})
# people('홍길동', 20)
#
# def add_and_mul(a, b):
#     return a+b
#
# def print_kwargs(**kwargs):
#      print(kwargs)
# print_kwargs(a=1, b=3, c=5, d='D')
#
# def all_sum(*arge):
#     print(args)
#
# def add(a, b):
#     return a + b
#
#
# def say():
#     return "Hi"
#
# def empty():
#     pass
# print(empty())

#클레스 class
#1. 클레스는 자신만의 데이터 타입을 정의하는 것
#2. 클레스틑 붕어빵 틀, 데이터의 형식을 정의하고,
# 틀에서 붕어빵은 실체가 된다.
# 클레스 -> 붕어빵 틀, 인스턴스(instance) -> 붕어빤
#class 클레스 이름:
#<클레스의 내용>
#<클레스의 내용>,,,
# 3.클레스는 자신의 인스턴스를 생성할떄 '생성자'라고 불리는 함수 호출함.
# 4.클래스는 상옥을 받을 수 있따.
# 클래스 이름(상속 받을 클래스 이름)
#5.클래스는 부몸의 멤버 메소드를 제작성 할 수 있다.(override)
#6.클래스는 연산자의 기능을 제작성 할 수 있다.(연사자 override)
# <...>
class Calculator:
    def __init__ (self):
          print('사칙연산 계산기의 생성자 호출')
    def add(self, a,b):
        return a+b
        return self.result

    def sub(self, a, b):
        return a - b
    def mul(self, a, b):
        return a * b
    def div(self, a, b):
        return a / b
class Upgreade(Calculator):
    def __init__(self):
        super(). __init__()
        print('업그레이드 계산기의 생성자 호출')
        pass
    def mod(self, a, b):
        return a % b
#StackElement 클래스 정의
class StackElement:
    #자기 자신의 아래쪽 링크를 정의해야 함(next)
    pass
    def __init__(self, value, next):
        self.value = value
        self.next = next
class Stack:
    #맨 위의 stackElement를 링크해야함
    #push스택의 맨 위에 데이터를 쌓는 것
    #pop스택의 맨위의 데이터를 삭제하는 것
    #peak스택의 맨위의 덷이터를 보는 것
    def __init__(self):
        self.top = None
        pass
    def push(self,value):
        pass
        if self.top is None:
            elem = StackElement(value, None)
            self.top = elem
        else:
            elem = StackElement(value, self.top)
            self.top = elem

    def pop(self):
        if self.top is None:
            return None
        else:
             pop_elem = self.top
             self.top = self.top.next
             return pop_elem.value
        pass

    def peek(self):
        if self.top is None:
            return None
        else:
            return self.top.value

stk = Stack()
stk.push(1)
stk.push(2)
stk.push(3)
print(stk.pop())
print(stk.pop())
print(stk.pop())
print(stk.pop())
elem2 = StackElement(1,None)
elsm1 = StackElement
# class 붕어빵:
#     def __init__(self, taste):
#         self.taste = taste
#     def print_taste(self):
#         print(f'{self.taste}맛 붕어빵')
# 붕어빵1 = 붕어빵('팥')
# 붕어빵2 = 붕어빵('크림')
# 붕어빵1.print_taste()
# 붕어빵2.print_taste()