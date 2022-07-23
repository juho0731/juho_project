# 1. 리스트는 정렬이 되어 있어야 한다.
# 2. 리스트의 시작과 끝은 left, right로 지정한다.
# 3. (left + right) // 2를 middle로 지정한다.
# 4. middle 이 찾고자 하는 값이랑 같으면 해당 위치를 리턴한다.
# 5. 값이 다른 경우
#   5-1. middle 보다 찾는 값이 크다. left = middle + 1
#   5-2. middle 보다 찾는 값이 작다. right = middle  - 1
#   5-3. 위를 수행후 3번부터 다시 수행
# 6. left > right 가 되는 경우 값을 찾지 못한 것으로 None 을 리턴
def binary_search(_list, data):
    right = len(_list)-1
    left = 0
    while left < right:
        middle = (right + left)//2

        if _list[middle] == data:
            return middle
        elif middle > data:
            right = middle - 1
        else:
            left = middle +1

a = [1,3,5, 7, 9, 11, 13, 15, 17, 19, 21]
position1 = binary_search(a, 11)
position2 = binary_search(a, 12)
print(position1, position2)