# 순차 탐색
# def sequential_search(datalist, targetData):
#     for index, data in enumerate(datalist):
#         if data == targetData:
#             return index
#     return None
# print(sequential_search([1,2,3,4,5], 5))

#이진 탐색
# def binary_search(datalist, targetData):
#     left = 0
#     right = len(datalist) - 2
#     while left <= right:
#         middle = (left + right) // 2
#
#         if datalist[middle] == targetData:
#             return middle
#
#         elif datalist[middle] < targetData:
#             left = middle + 1
#
#         else:
#             right = middle - 1
#
#     return None
#
# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 18, 19, 21, 24, 37, 40, 45, 71]
# print(binary_search(array, 7))

# def binary_search(datalist, targetData, left, right):
#     if left > right:
#         return None
#     middle = (left + right) // 2
#     if datalist[middle] == targetData:
#             return middle
#     elif datalist[middle] < targetData:
#             return binary_search(datalist, targetData, middle +1, right)
#
#     else:
#             return binary_search(datalist, targetData, left, middle - 1)
#
# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 18, 19, 21, 24, 37, 40, 45, 71]
# print(binary_search(array, 7, 0, len(array)-1))

# def solution(n, times):
#     # 최소 시간
#     left = 1
#
#     # 최대 시간
#     right = n * max(times[-1])
#     while left <= right:
#         middle = (left+right) // 2
#
#         # middle 시간 동안 처리할 수 있는 입국자
#         arrivals = 0
#         for t in times:
#             arrivals += (middle // t)
#
#         # n명의 입국자를 처리해야 하는데,
#         # 계산된 입국자가 n보다 작다면?
#         if arrivals < n:
#             left = middle + 1
#         #계산된 입국자가 n보다 크거나 작다면?
#         else:
#             right = middle - 1
#     return left #최소 시간

# 깊이우선 탐색
#
# def DFS(martrix, start_node):
#     visit = [False] * len(martrix)
#     stack = []
#
#     stack.append(start_node)
#     visit[start_node] = True
#     print("방문", start_node)
#
#     while stack:
#         node = stack.pop()
#         for next_node in range(len(martrix)):
#             if martrix[node][next_node] == 1:
#                 if not visit[next_node]:
#                     stack.append(next_node)
#                     visit[next_node] = True
#                     print("방문", next_node)
#
# amatrix = [
#     [0, 1, 1, 0, 0],
#     [1, 0, 1, 1, 0],
#     [1, 1, 0, 0, 0],
#     [0, 1, 0, 0, 1],
#     [0, 0, 0, 1, 0]
# ]
#
# DFS(amatrix, 0)

visit = {}

def DFS(matrix, node):
    visit[node] = True
    print("방문", node)
    for next_node in range(len(matrix)):
        if matrix[node][next_node] == 1:
            if next_node not in visit:
                DFS(matrix, next_node)

amatrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0]
]