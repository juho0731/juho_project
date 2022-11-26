# # 벨먼-포드 알고리즘 함수
# # matrix: 가중치 입접 행렬
# # start: 시작 노드
# def bdllman_ford(matrix, start):
#     # 노드의 개수
#     v = len(matrix)
#
#     # 1. 최단 거리 테이블 초기화
#     distance = [float('inf')] * v
#
#     # 2. 출발 노드 설정
#     distance[start] = 0
#
#     # 3. 모든 노드에 대하여 최소 비용 계산
#     # (v 번, 마지막 음의 사이클 검사까지 포함함)
#     for n in range(v):
#         for x in range(v):
#             for y in range(v):
#                 cost = matrix[x][y]
#
#                 # 최소 비용 갱신
#                 # 원래라면 distance[x] != float('inf')를 검사해야 한다.
#                 # 여기서 검사하지 않은 이유는 어짜피 inf + x == inf 이기 때문
#                 if distance[y] > distance[x] + cost:
#                     distance[y] = distance[x] + cost
#
#                     # 4. v번째에 갱신이 발생했다면 최단 거리를 구할 수 없음
#                     if n == v - 1:
#                         return False, distance
#
#     return True, distance
#
# inf = float('inf')
# amatrix = [
#     [0, 7, 5, 3, inf],
#     [inf, 0, inf, inf, inf],
#     [inf, inf, 0, 3, 3],
#     [inf, 3, inf, 0, -6],
#     [inf, inf, 2, inf, 0]
# ]
#
# success, distance = bdllman_ford(amatrix, 0)
# print('최단 경로의 존재:', success)
# print('마지막 계산된 최단 경로:', distance)
#
# amatrix2 = [
#     [0, 3, 5, 1, inf],
#     [inf, 0, inf, inf, 4],
#     [inf, inf, 0, -3, -3],
#     [inf, -2, inf, 0, -1],
#     [inf, inf, inf, inf, 0]
# ]
#
# success, distance = bdllman_ford(amatrix2, 0)
# print('최단 경로의 존재:', success)
# print('마지막 계산된 최단 경로:', distance)

# 타임머신 - 백준 11657번

import sys

def bellman_ford(v, matrix, start):

    distance = [float('inf')] * (v+1)
    distance[start] = 0

    for n in range(v):
        for x, y, cost in matrix:
            if distance[y] > distance[x] + cost:
                distance[y] = distance[x] + cost
                if n == v - 1:
                    return [-1]

    return distance[2:]

N, M = map(int, sys.stdin.readline().split())

alist = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]

dist = bellman_ford(N, alist, 1)

for d in dist:
    print(d if float('inf') > d else -1)

