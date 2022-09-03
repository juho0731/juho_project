class ArithmetiticAddlist(list):
    def __init__(self, data=()):
        super().__init__(data)

    def __add__(self, other):
        if len(self) != len(other):
            raise Exception("리스트의 길이가 다릅니다.")
        result = ArithmetiticAddlist()

        for item1, item2 in zip(self, other):
            result.append(item1 + item2)

        return result


alist1 = ArithmetiticAddlist([1, 2, 3])
alist2 = ArithmetiticAddlist([4, 5, 6])
alist3 = alist1 + alist2
print(alist3)

#왼쪽피연산자가 오른쪽 피연산자 보다 작거나 같은지 비교
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

pt1 = Point(1,2)
pt2 = Point(1,2)
pt3 = Point(2,3)

print(pt1 == pt2)
print(pt2 == pt3)
print(pt2 != pt3)

#인덱스 연산자 오버로딩

class ThreeItem:
    def __init__(self, item1, item2, item3):
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3
    def __getitem__(self, item):
        if item == 0:
            return self.item1
        elif item == 1:
            return self.item2
        elif item == 2:
            return self.item2
        else:
            raise IndexError("0~2까지의 값만 참조할 수 있습니다.")


#노드 클랫 구현하기

class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

b = Node(2)
a = Node(1,b)
print(a.data)
print(a.link.data)
print(a.link.link)

#MyList클래스 작성

# class MyList:
#     def __init__(self, *args):
#         self.head = None
#         self.tail = None
#         self.lenght = 0


class MyList:
    def __init__(self, *args):
        self.head = None
        self.tail = None
        self.lenght = 0
        for arg in args:
            self.append(arg)

    def append(self, data):
        # 새로운 노드 생성
        node = Node(data)
        # 리스트가 비어 있는 경우
        if self.head is None:
            self.head = node
            self.tail = node
        # 리스트가 비어있지 않은 경우
        else:
            self.tail.link = node
            self.tail = node
        #연결 후 길이를 늘여준다
        self.lenght += 1

    def __iter__(self):
        def gen():
            curr = self.head
            while curr is not None:
                yield curr.data
                curr = curr.link
        return gen()

    def __len__(self):
        return self.lenght
    def __str__(self):
        s = "<"
        for idx, data in enumerate(self):
            s += str(data)
            if idx < len(self)-1:
                s += ", "
            else:
                s += ">"
        return s
    def __getitem__(self, item):
        if type(item) is not int:
            raise TypeError("인덱스는 반드시 정수여야 합니다.")
        if item < 0:
            item = len(self) + item
        if item >= len(self) or item < 0:
            raise  IndexError("인덱스 범위를 벗어났습니다.")
        for idx, data in enumerate(self):
            if idx == item:
                return data
    def __setitem__(self, key, value):
        if type (key) is not int:
            raise TypeError("인덱스는 반드시 정수여야 합니다.")

        if key < 0:
            item = len(self) + key

        if key >= len(self) or key < 0:
            raise IndexError("인덱스 범위를 벗어났습니다.")
        #데이터를 바꾸려면 노드에 직접 접근한다.
        curr = self.head
        #key만큼 링크를 이동시켜서 데이터를 바꾼다.
        for i in range(key):
            curr = curr.link
        curr.data = value
mylist = MyList(1,2,3,4)
mylist[3] = 5
print(mylist[3])