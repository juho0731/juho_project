def solution(numlist, n):
    answer = []

    for i in range(len(numlist)):
        d = n - numlist[i]
        if d < 0:
            d = -d
        numlist[i] = [d, numlist[i]]
    numlist.sort()

    for i in range(len(numlist)):
        if numlist[i-1][0] == numlist[i][0] and numlist[i-1][1] < numlist[i][1]:
            answer.insert(i-1, numlist[i][1])
        else:
            answer.append(numlist[i][1])
    return answer

# def solution(numlist, n):
#     numlist.sort(key=lambda x: (abs(n-x), -x))

