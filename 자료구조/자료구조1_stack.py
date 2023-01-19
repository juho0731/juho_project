class StackElement:
    #자기 자신의 아래쪽 링크를 정의해야 함(next)
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
