class dequeElement:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

class deque:
    def __init__(self):
        self.rear = None
        self.front = None

    def insert_rear(self,value):
        e = dequeElement(value, left=None,right = self.rear)
        if self.front is None:
            self.rear = e
            self.front = e
        else:
            self.rear.left = e
            self.rear = e

    def insert_front(self,value):
        e = dequeElement(value, right=None, left=self.front)
        if self.rear is None:
            self.front = e
            self.rear = e
        else:
            self.front.right = e
            self.front = e

    def delete_rear(self):
        if self.front == None:
            return None
        value = self.rear.value
        if self.rear == self.front:
            self.rear = self.front = None
        else:
            self.rear = self.rear.right
            self.rear.left = None
        return value


    def delete_front(self):
        if self.rear == None:
            return None
        value = self.front.value
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.right
            self.front.right = None
        return value

    def reverse(self):
        curr = self.rear
        while curr is not None:
            curr.left, curr.right = curr.right, curr.left
            curr = curr.left
        self.rear, self.front = self.front, self.rear

d = deque()

for i in range(1, 6):
    d.insert_rear(i)
    d.insert_front(-i)
d.reverse()
for i in range(10):
    print(d.delete_rear())