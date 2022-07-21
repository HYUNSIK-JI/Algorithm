import sys

#입력  시간을 줄이기 위함
input = sys.stdin.readline

n = int(input())

#연산 횟수를 저장하는 공간
dp = [0] * (n + 1)

for i in range(2, n + 1):
    dp[i]=dp[i - 1] + 1

    #x가 2으로 나누어 떨어지면
    if i%2 == 0:
        dp[i]=min(dp[i],dp[i // 2]+1)
    #x가 3으로 나누어 떨어지면
    if i%3 == 0:
        dp[i]=min(dp[i],dp[i // 3]+1)

print(dp[n])