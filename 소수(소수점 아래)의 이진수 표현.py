#이진수 소수 → 십진수 소수 변환기

# def b(a):
#     c = 0
#     for i in range(len(a)):
#         c += int(a[i])*2**-(i+1)
#     print(c)

# a = input()
# b(a)

#십진수 소수 → 이진수 소수 변환기

# def point_dtob(decimal):
#     divisor = 10
#     while divisor < decimal:
#         divisor *= 10
#
#     binary = ""
#     while decimal > 0 and len(binary) < 23:
#         decimal *= 2
#         binary += str(decimal // divisor)
#         decimal %= divisor
#     return binary
#
# decimal = int(input())
# print(point_dtob(decimal))
