#리스트 컴프리헨션
# squares = [X**2 for X in range(10)]
#
# vec = [-4. -2, 0, 2, 4]
# [X for X in vec if X >=0]
# [abs(X) for X in vec]
#
# fruits = [' apple ', ' banana ', ' coconut ']
# [f.strip(for f in fruits)]
#
# [(X, X**2)for X in range(6)]
#
# vec = [[1,2,3],[4,5,6],[7,8,9]]
# [num for elem in vec for num in elem]

#중첩된 리스트 컴프리헨션
# matrix = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]

# transposed = [[row[i] for row in matrix]for i in range(4)]

# transposed = []
# for i in range(4):
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)

# print(list(zip(*matrix)))
# 리스트 앞의 *은 unpacking 연산자이다.

# import sys
# n = int(sys.stdin.readline())
# stack = [int(sys.stdin.readline())for _ in range(n)]
# count = 0
# max_stick = 0
#
# while stack:
#     stick = stack.pop()
#     if stick > max_stick:
#         max_stick = stick
#         count += 1
# print(count)

import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque([num for num in range(1, n+1)])

t = 1
while len(queue) != 1:
    k = t**3%len(queue)
    for i in range(k):
        x = queue.popleft()
        queue.append(x)
    queue.pop()

    t += 1
print(queue[0])


