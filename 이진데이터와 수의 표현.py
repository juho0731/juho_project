# import sys
#
# a = sys.stdin.readline()
# c = 0
# for i in range(len(a)-1):
#     if int(a[i]) == 1:
#         c += 2**(len(a)-2-i)
# print(c)

# binary = input()
# decimal = 0
# for i, bit in enumerate(reversed(binary)):
#     decimal += int(bit) * (2**i)
# print(decimal)
#
# decimal = int(input())

# decimal = int(input())
# binary = ''
# while decimal > 0:
#     binary += str(decimal % 2)
#     decimal = decimal // 2
# binary = binary[::-1]
# print(binary)

# binary = input()
# #1의 보수를 구한다.
# comp1 = ""
# for bit in binary:
#     comp1 += "1" if bit == "0" else "0"
#
# # 2의 보수를 구한다.
# comp2 = ""
# carry_bit = 1 # 올림수
# for bit in reversed(comp1):
#     if bit == "1" and carry_bit == 1:
#         comp2 += "0"
#         carry_bit = 1
#     elif bit == "0" and carry_bit == 1:
#         comp2 += "1"
#         carry_bit = 0
#     else:
#         comp2 += bit
# comp2 = comp2[::-1]
# print(comp2)

def binary_to_decimal(binary):
    decimal = 0
    for i, bit in enumerate(binary[::-1]):
        decimal += int(bit) * (2**i)
    return decimal

def twos_complement(binary):
    #1의 보수를 구한다.
    comp1 = ""
    for bit in binary:
        comp1 += "1" if bit == "0" else "0"

    # 2의 보수를 구한다.
    comp2 = ""
    carry_bit = 1 # 올림수
    for bit in reversed(comp1):
        if bit == "1" and carry_bit == 1:
            comp2 += "0"
            carry_bit = 1
        elif bit == "0" and carry_bit == 1:
            comp2 += "1"
            carry_bit = 0
        else:
            comp2 += bit
    return comp2[::-1]

binary = input()

sign = 1

if binary[0] == "1":
    binary = twos_complement(binary)
    sign = -1

decimal = binary_to_decimal(binary)
decimal = decimal * sign
print(decimal)
