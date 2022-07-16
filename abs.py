#abs
#absoluted
#숫자의 절댓값
# print("1의 절댓값",abs(1)) #1
#
# print("-3의 절댓값",abs(-3)) #3
#
# print("-.5의 절댓값",abs(-.5)) #0.5

class Mylist(list):
    def __init__(self, seq=()):
        super().__init__(seq)

    def __abs__(self):
        abslist = Mylist()
        #숫자만 abs로 적용하여 새로운 리스트 생성
        for val in self:
            if type(val) in (int, float):
                abslist.append(abs(val))
            else:
                abslist.append(val)

        return abslist

mylist = Mylist([-1,-2,-3,'4'])
print(abs(mylist))