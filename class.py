class AAA:
    share = 10
    def __init__(self, value):
        self.unique = value

a = AAA(1)
b = AAA(2)
print(a == b)
print(a.unique == b.unique)
print(a.share == b.share)
AAA.share = 0
print(a.share == b.share)
a.share = 5
print(a.share == b.share)

class Animal:
    def pattern(self):
        print("민무늬")

    def sound(self):
        print("소리없음")

class Dog(Animal):
    def sound(self):
        print("멍멍")
d = Dog()
d.pattern()
d.sound()
# class Dog(Animal):
#     def sound(self):
#         Animal.sound(self)
#         print("멍멍")

# class Dog(Animal):
#     def sound(self):
#         super.sound()
#         print("멍멍")

class Reserve:

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index-1
        return self.data[self.index]

rev = Reserve("Hello")

for char in rev:
    print(char)

def generator_test():
    yield 1
    yield 2
    yield 3

it = generator_test()
print(next(it))
print(next(it))
print(next(it))

def reverse(data):
    for i in range(len(data)-1, -1, -1):
        yield data[i]

for char in reverse('world'):
    print(char)

# 세 종류의 값을 저장하는 클래스
class Value3:
    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    def __iter__(self):
        def gen_iter():
            yield self.v1
            yield self.v2
            yield self.v3
        return gen_iter()

value3 = Value3("문자열", 1000, ("튜플", 1))

# 1.in 오른쪽 객체에 대한 iter 메서드 호출
# 2. iterator 객체에서  next 메서드 호출
# 3. 2번을 StopIteration 예외 발생 까지 반복
for i in value3:
    print(i)