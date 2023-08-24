class Node:
   def __init__(self,data,link = None):
      self.data = data
      self.link = link
class MyList:
    def __init__(self, *args):
        self.head = None
        self.tail = None
        self.length = 0
        for arg in args:
            self.append(arg)

    def append(self, data):
        # 새로운 노드 생성
        node = Node(data)

        # 리스트가 비어있는 경우
        if self.head is None:
            self.head = node
            self.tail = node
        # 리스트가 비어있지 않은 경우
        else:
            self.tail.link = node
            self.tail = node
        # 연결 후 길이를 늘려준다
        self.length += 1

    def __str__(self):
        result = "<"  # 연결 리스트의 시작부분
        curr = self.head
        while curr is not None:
            result += str(curr.data)
            if curr.link is not None:
                result += ", "
            curr = curr.link

        result += ">"  # 연결 리스트의 끝 부분
        return result

    def __iter__(self):
        def generate():
            curr = self.head
            while curr is not None:
                yield curr.data
                curr = curr.link

        return generate()

    def __len__(self):
        return self.length

    def __getitem__(self, item):
        if type(item) != int:
            raise TypeError(f'list indices must be integers or slices, not {type(item).__name__}')
        if item < 0:
            item = len(self) + item
        if self.length<0 or self.length < item:
            raise IndexError(f'list index out of range')
        for idx, value in enumerate(self):
            if idx == item:
                return value

    def __setitem__(self, key, value):
        if type(key) != int:
            raise TypeError(f'list indices must be integers or slices, not {type(key).__name__}')
        if key < 0:
            key = len(self) + key
        if self.length < 0 or self.length < key:
            raise IndexError(f'list index out of range')

        cnt = 0
        curr = self.head
        while cnt != key:
            curr = curr.link
            cnt += 1
        curr.data = value

    def pop(self, idx=-1):
        if type(idx) != int:
            raise TypeError(f'list indices must be integers or slices, not {type(idx).__name__}')
        if idx < 0:
            idx = len(self) + idx
        if self.length < 0 or self.length < idx:
            raise IndexError(f'list index out of range')

        self.length -= 1
        if self.head == self.tail:
            ret_data = self.head.data
            self.head = self.tail = None
            return ret_data
        else:
            if idx == 0:

                ret_data = self.head.data
                self.head = self.head.link
                return ret_data
            elif idx == len(self):

                ret_data = self.tail.data
                curr = self.head
                while curr.link != self.tail:
                    curr = curr.link
                self.tail = curr
                curr.link = None
                return ret_data
            else:
                curr = self.head
                for _ in range(idx-1):
                    curr = curr.link
                ret_data = curr.link.data
                curr.link = curr.link.link
                return ret_data



list = MyList(1,2,3,4,5)
print(list.pop(2))
print(list)
print(list.pop(0))
print(list)
print(list.pop(1))
print(list)
print(list.pop(1))
print(list)
print(list.pop())
print(list)