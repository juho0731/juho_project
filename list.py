class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class Mylist:
    def __init__(self, *datas):
        self.lenght = 0
        self.head = None
        self.tail = None
        for data in datas:
            self.append(data)
    def append(self,data):
        if self.head == None:
            node = Node(data)
            self.head = node
            self.tail = node
        else:
            node = Node(data)
            self.tail.link = node
            self.tail = node
        self.lenght += 1

    def __str__(self):
        result = '<'
        curr = self.head
        while curr:
            result += str(curr.data)
            if curr != self.tail:
                result += ', '
            curr = curr.link
        result += '>'
        return result

    def __len__(self):
        return self.lenght


arr = Mylist(1,2,3,4)
arr.append(5)
print(arr)