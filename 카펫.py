def solution(brown, yellow):
    total = brown + yellow
    for tx in range(3, total // 3 + 1):
        ty = total // tx
        if tx * ty == total and (tx-2) * (ty-2) == yellow:
            return [max(tx, ty), min(tx, ty)]

