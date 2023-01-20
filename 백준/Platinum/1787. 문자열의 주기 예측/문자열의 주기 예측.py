from math import inf

def dfs(i): # 풀이에서 말했던 pi[pi[i] - 1] 를 차례대로 찾아가는 함수
    if i < 0 or not pi[i]: # 인덱스가 0보다 작아지거나 pi[i] 가 0이면 멈춘다.
        return inf
    if dp[i] > -1: # 메모이제이션 기법으로, i에서의 결과를 전에 구한 적 있으면 다시 꺼내 쓴다.
        return dp[i]
    dp[i] = min(pi[i], dfs(pi[i] - 1)) # 가장 짧은 길이를 구해 dp[i]에 저장한 다음, 반환
    return dp[i]

n = int(input())
S = input().strip()

# 실패 함수
pi = [0] * n
i = 0
for j in range(1, n):
    while i and S[i] != S[j]:
        i = pi[i - 1]
    if S[i] == S[j]:
        i += 1
        pi[j] = i

dp = [-1] * n
answer = 0
for i in range(n):
    result = dfs(i)
    if result < inf: # inf가 나오면 길이를 구하지 못했다는 것이므로 (주기가 없다는 것이므로) 패스
        answer += i + 1 - result # i는 인덱스이므로 실제 위치 값은 i + 1. 그러므로 (i + 1 - 최단 길이)를 합에 더해줘야 한다.
print(answer)