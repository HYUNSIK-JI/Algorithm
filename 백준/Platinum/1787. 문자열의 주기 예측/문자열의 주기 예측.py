def dfs(i):
    if i < 0 or not pi[i]:
        return 1e9
    if dp[i] > -1:
        return dp[i]
    dp[i] = min(pi[i], dfs(pi[i] - 1))
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
    if result < 1e9:
        answer += i + 1 - result
print(answer)
