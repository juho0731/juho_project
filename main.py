# 2부터 120까지의 수들중에서 소수는 몇개이고 누구누구 인가?
# 2부터 120까지를 담은 수열을 만든다.
arr = [True] * 121 # arr[x] == 정수 x가 소수인지 아닌지의 값이 들어있다.
# 2부터 120까지 숫자를 증가시키면서 2의 배수들을 False로 변환한다.
# 2의 배수들을 다 봤으면 그다음 3을 제외한 3의 배수들을 False로 변경한다.
# 이미 False인 애들은 배수를 구하지 않는다.
n = int(input()) # n까지의 수들중 소수가 몊개인지 구하고, 소수 리스트도 출력한다.
arr[:2] = [False, False]
for i in range(2, int(n**0.5)+1):
    if arr[i]:
        for j in range(i+1, n+1, i):
            arr[j] = False
print(arr.count(True))
