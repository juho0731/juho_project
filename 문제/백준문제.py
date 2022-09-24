# import sys
# n, m = map(int, sys.stdin.readline().split())
#
# s = {sys.stdin.readline()for _ in range(n)}
# count = 0
# for _ in range(m):
#     if sys.stdin.readline() in s:
#         count += 1
# print(count)

# s = input()
# check = {chr(a): -1 for a in range(ord('a'),ord('z')+1)}
# for i, c in enumerate(s):
#     if check[c] == -1:
#         check[c] = i
# print(*check.values())

# import sys
#
# cache = {1: 1, 2: 1, 3: 1}
# def p(n):
#     if n in cache:
#         return cache[n]
#     cache[n] = p(n-3) + p(n-2)
#     return cache[n]
#
# t = int(sys.stdin.readline())
# for _ in range(t):
#     n = int(sys.stdin.readline())
#     print(p(n))

