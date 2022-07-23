# class range(stop)
# class range(start, stop [,step])
# 함수가 아닌 형식.
# 1. stop 만 입력한 경우: 0부터 stop -1까지의 시퀀스 생성
# 2. strat, stop 입력한 경우: start 부터 stop - 1 까지의 시퀀스 생성
#   2-1. 추가로 step 입력한 경우: start ~ stop -1 까지 step 씩 시퀀스

print(list(range(4)))         #stop 만 입력
print(list(range(1, 4)))      #start, stop 입력
print(list(range(1, 4, 2)))   #추가로 step 입력