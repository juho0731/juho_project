class TreeNode:
    def __init__(self,value, left, right):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = TreeNode(value, None, None)
        if self.root is None:
            self.root = node
            return
        curr = self.root
        while True:
            if value >= curr.value:
                if curr.right is None:
                    curr.right = node
                    return
                curr = curr.right
            else:
                if curr.left is None:
                    curr.left = node
                    return
                curr = curr.left


    def find(self, value):
        curr = self.root
        while curr:
            if curr.value == value:
                return True
            elif curr.value < value:
                curr = curr.right
            else:
                curr = curr.left
        return False



    def delete(self, value):
        parent = None
        curr = self.root
        while curr:

            if curr.value == value:
               if curr.right == None and curr.left == None:     #curr의 자식이 없을 경우
                   if parent.left == curr:
                       parent.left = None
                   else:
                       parent.right = None
                   return curr.value
               elif curr.right is None and curr.left is not None:       #curr의 자식이 하나인 경우(left만 있는 경우)
                    if parent.left == curr:
                        parent.left = curr.left
                    else:
                        parent.right = curr.left
               elif curr.left is not None and curr.left is None:        #curr의 자식이 하나인 경우(right만 있는ㄴ 경우)
                   if parent.left == curr:
                       parent.left = curr.right
                   else:
                       parent.right = curr.right
               #삭제 하려는 노드의 자식 노드가 두개인 경우(왼쪽 서브트라의 제일 오른쪽 값을 삭제할 노드의 복사)
               else:
                    ret_value = curr.vlaue
                    succ_p = None
                    succ = curr.left
                    while succ.right is None:
                        succ_p = succ
                        succ = curr.right
                    curr.value = succ.value
                    succ_p.right = succ.left
                    return ret_value
               return curr.value
            elif curr.value < value:
                parent = curr
                curr = curr.right
            else:
                parent = curr
                curr = curr.left
        return None

