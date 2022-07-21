import sys

#입력 시간을 줄이기 위함
input = sys.stdin.readline

#과자 하나당 가격,사려고하는 과자의 개수,내가 가진돈
k,n,m = map(int,input().split())

#부모님에게 받아야 할 돈 계산
answer = (k * n) - m

#마이너스면 0
if answer<0:
    print(0)
else:
    print(answer)