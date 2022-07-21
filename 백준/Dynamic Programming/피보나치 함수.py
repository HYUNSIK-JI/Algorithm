import sys

#입력 시간을 줄이기 위함
input = sys.stdin.readline

# DP를 활용하기 위한 리스트
dp = [[1,0],[0,1],[1,1]]

#점화식
# dp[i] = (dp[-2][0] + dp[-1][0] , dp[-2][1] + dp[-1][1])

#N의 범위가 40까지이므로 41까지 설정
# 테스트케이스 마다 반복문을 돌려 계산하는 것보다 먼저 계산후 출력하는 것이 시간적인 효율성에 있어서 월등하므로 먼저 계산

for i in range(3,41):
    #0이 나올 횟수 와 1이 나올 횟수 계산을 위한 점화식 활용
    dp.append((dp[-2][0] + dp[-1][0] , dp[-2][1] + dp[-1][1]))
for test_case in range(int(input())):
    #해당 n에 대해 0,1이 나올 횟수 출력을 위한 n값 입력
    n = int(input())

    #출력
    print(dp[n][0], dp[n][1])