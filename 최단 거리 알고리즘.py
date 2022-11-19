# class MInHeap:
#     def __init__(self):
#         self.tree = [float('-inf')]
#
#     def insert(self, data):
#         # 1.제일 마지막 터미널 노드에 테이터 삽입
#         self.tree.append(data)
#
#         # 2. 삽입 노드와 부모 노드 비교 및 교환
#         idx = len(self.tree) - 1 # 삽입 노드의 인덱스
#         while self.tree[idx//2] > self.tree[idx]:
#             self.tree[idx], self.tree[idx//2] = self.tree[idx//2], self.tree[idx]
#
#     def delete(self):
#         # 트리가 비어있는 경우  None 반환
#         if len(self.tree) == 1:
#             return None
#
#         # 1. 루트 노드의 값을 저장
#         data = self.tree[1]
#
#         # 2. 가장 마지막 터미널 노드의 값을 루프 노드에 복사
#         self.tree[1] = self.tree[-1]
#         self.tree.pop()
#
#         idx = 1 # 현재 노드의 인덱스
#         while True:
#             # 왼쪽 자식 노드의 인덱스
#             c_idx = idx*2
#
#             # 오른쪽 자식 노드가 존재하면서, 더 작으면 오른쪽 자식 노드 선택
#             if c_idx + 1 < len(self.tree):
#                 c_idx += 1
#
#             # 인덱스 범위가 벗어나거나 자식보다 부모가 더 작으면 멈춤
#             if c_idx >= len(self.tree) or self.tree[c_idx] > self.tree[idx]:
#                 break
#
#             # 선택된 자식 노드와 현재 노드 교환
#             self.tree[idx], self.tree[c_idx] = self.tree[c_idx], self.tree[idx]
#
#         #마지막으로 데이터 반환
#         return data
#
#
# test = MInHeap()
# input_data = [1, 3, 5, 7, 9, 2, 4, 6]
# for n in [1, 3, 5, 7, 9, 2, 4, 6]:
#     test.insert(n)
# print(test.tree)
#
# output_data = []
# for _ in input_data:
#     output_data.append(test.delete())
# print(output_data)

# import heapq
#
# # 다익스트라 알고리즘 함수
# # matrix: 가중치 인접 행렬
# # start: 시작 노드
# def dijkstra(matrix, start):
#     # 1. 최단 거리 테이블 초기화, 방문 표시 테이블 초기화
#     distance = [float('inf')for _ in range(len(matrix))]
#     visit = [False for _ in range(len(matrix))]
#
#     # 우선순위 큐(최소 힙) 준비
#     pq = []
#
#     # 2. 출발 노드 설정 (간선 가중치와 노드 번호를 같이 넣어준다.)
#     heapq.heappush(pq, (0, start))
#
#     distance[start] = 0
#
#     while pq:
#         # 3. 방문하지 않은 가장 비용이 적은 node를 선택
#         cost, node = heapq.heappop(pq)
#
#         # 만약 이미 처리된 노드라면 넘어감
#         if visit[node]:
#             continue
#
#         visit[node] = True
#
#         # 4. 출발 노드 -> 선택 노드를 거쳐 가는 경우를 고려하여 최소 비용 갱신
#         for i in range(len(matrix[node])):
#             if distance[i] > matrix[node][i] + cost:
#                 distance[i] = matrix[node][i] + cost
#                 heapq.heappush(pq, (distance[i], i))
#
#     return distance
#
# inf = float('inf')
# amatrix = [
#     [0, 3, 4, inf, inf, inf],
#     [3, 0, inf, inf, 8, inf],
#     [4, inf, 0, 1, 10, inf],
#     [inf, inf, 1, 0, inf, 2],
#     [inf, 8, 10, inf, 0, inf],
#     [inf, 6, inf, 2, inf, 0]
# ]
#
# dist = dijkstra(amatrix, 0)
# print(dist)

import heapq
import sys

# 정점의 개수 V와 간선의 개수 E
V, E = map(int, sys.stdin.readline().split())

# 시작 정점의 번호 K
K = int(sys.stdin.readline())

# 간선 연결 정보 L
L = [[]for _ in range(V+1)]
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    L[u].append((v, w))

# 최단 거리 테이블
dist = [float('inf')] * (V + 1)
# 방문 표시 집합
visit = [False] * (V + 1)

# 우선 순위 큐
pq = []

heapq.heappush(pq, (0, K))
dist[K] = 0

while pq:
    cost, node = heapq.heappop(pq)

    if visit[node]:
        continue

    visit[node] = True

    for n_node, n_cost in L[node]:
        if dist[n_node] > n_cost + cost:
            dist[n_node] = n_cost + cost
            heapq.heappush(pq, (dist[n_node], n_node))

for i in dist[1:]:
    print(i if i < float('inf')else 'INF')

