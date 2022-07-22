# m이 n 보다 크기 때문에 최대 연결할 수 있는 다리의 개수는 n개이다.
# m개의 지역에 n개의 다리를 놓을 수 있는 경우의 수를 구하는 것이기 때문에
# mCn 으로 표현 할수 있고 이는 m!을 (m-n)!n!으로 나눈 값이 된다.

import sys

input = sys.stdin.readline

# n, m 의 범위가 0~30 까지이다.
# dp = [0] * 31 으로 저장하지 않는 이유는 mCn을 표현한 식에서 나누기 부분에서 0으로 나눌순 없기 때문이다.
dp = [1] * 31

#n! 값을 미리 저장
dp[1], dp[2] = 1, 2

for i in range(3, 31):
    # m!을 표현 하는 점화식
	dp[i] = dp[i - 1] * i

for test_case in range(int(sys.stdin.readline())):
    #n,m 입력
	n,m = map(int, input().split())

    # mCn을 m! // (m-n)! * n!으로 표현
	answer = dp[m] // (dp[m - n] * dp[n])
	print(answer)