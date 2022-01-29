def ceil(num):  # num = 소수점이 포홤된,또는 포함되지 않은 숫자(올림함수)
    if int(num) < num:
        return int(num) + 1
    return int(num)


def solution(progresses, speeds):
    # 가능이 완성되기 까지 걸리는 기간
    terms = [ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    terms.reverse()  # 리스트 갑 뒤집기 함수

    top = terms.pop()
    count = [1]
    while terms:
        element = terms.pop()
        if element <= top:
            count[-1] += 1
        else:
            top = element
            count.append(1)
    return count
