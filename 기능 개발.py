a = []
def push():
    stack_list.append(value)

def pop():
    stack_list[len(stack_list)-1] = 0

def peek():
    print(stack_list[len(stack_list)-1])

stack_list=[]

push(13)
push(612)
push("abvc")
push("oop21")

print(stack_list)

pop()
pop()
peek