# 플로이드-워셜 알고리즘
# matrix: 인접 행렬
def floyd_warshall(matrix):
    # 정점의 개수
    v = len(matrix)

    # 1. 최단 거리 테이블 생성 및 초기값 설정
    d = [[float('inf')] * v for _ in range(v)]
    for x in range(v):
        for y in range(v):
            d[x][y] = matrix[x][y]

    # 2. 중간 지점 노드 m에 대하여 x -> m -> y 비용을 계산하며 최단 거리 갱신
    for m in range(v):
        for x in range(v):
            for y in range(v):
                d[x][y] = min(d[x][y], d[x][m] + d[m][y])

    return d


inf = float('inf')
amatrix = [
    [0, 3, inf, inf],
    [4, 0, 2, 4],
    [7, 5, 0, 3],
    [inf, inf, 1, 0]
]

dist = floyd_warshall(amatrix)
print(dist)

# 프로그래머스 순위 49191

def solution(n, results):
    # 최단거리 테이블 생성
    # (승패 유뮤만 따지면 되드모 inf 대신 0 을 사용)
    d = [[0] * (n+1) for _ in range(n+1)]

    # 최단 거리 테이블 초기화
    for x, y in results:
        d[x][y] = 1 # x가 y에게 이긴 경우
        d[y][x] = -1 # x에게 진 경우

    # 플로어드-워셜
    for m in range(1, n+1):
        for x in range(1, n+1):
            for y in range(1, n+1):
                # x가 m에게 이기고, m이 y에게 이긴 경우
                if d[x][m] == 1 and d[m][y] == 1:
                    d[x][y] = -1
                # x가 m에게 지고, m이 y에게 진 경우
                elif d[x][m] == -1 and d[m][y] == -1:
                    d[x][y] = -1

    # 자기 자신을 제외한 모든 노드에 대하여 승패가 결정되 경우 카운트
    # (0이 하나인 경우)
    answer = 0
    for x in range(1, n+1):
        zero_cnt = 0
        for y in range(1, n+1):
            zero_cnt += 1 if d[x][y] == 0 else 0
        if zero_cnt == 1:
            answer += 1


    return answer