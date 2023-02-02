class Node:
    def __init__(self, data, right, left):
        self.data = data
        self.right = right
        self.left = left
class Deque:
    def __init__(self):
        self.rear = None
        self.front = None

    def insert_rear(self, data):
        if self.rear is None:
            node = Node(data, None, None)
            self.rear = node
            self.front = node


        else:
            node = Node(data, None, self.rear)
            self.rear.left = node
            self.rear = node

    def insert_front(self, data):
        if self.front is None:
            node = Node(data, None, None)
            self.rear = node
            self.front = node

        else:
            node = Node(data, self.front, None)
            self.front.right = node
            self.front = node

    def delete_rear(self):
        if self.rear is None:
            return None

