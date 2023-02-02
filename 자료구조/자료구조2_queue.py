class Element:
    def __init__(self,value,link):
        self.value = value
        self.link = link

class Queue:
    def __init__(self):
        self.rear = None
        self.front = None
#rear에 데이터를 붙인다.
    def enQueue(self,value):
        if self.front is None:
            elem = Element(value, None)
            self.front = elem
            self.rear = elem
        else:
            elem = Element(value, None)
            self.rear.link = elem
            self.rear = elem

#front에서 데이터를 꺼낸다.
    def deQueue(self):
        if self.front is None:
            return None
        else:
            elem = self.front
            self.front = self.front.link
            return elem.value
# TODO: 데이터 순서 뒤집기
    def reverse(self):
       prev = None
       curr = self.front
       while curr:
          next = curr.link
          curr.link = prev
          prev = curr
          curr = next
       self.rear, self.front = self.front, self.rear

q = Queue()
for i in range(10):
    q.enQueue(i)
q.reverse()
for i in range(10):
    print(q.deQueue())
