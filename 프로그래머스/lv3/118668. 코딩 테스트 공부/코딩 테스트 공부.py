import sys
def solution(alp, cop, problems):
    INF = sys.maxsize;
    mx_alp, mx_cop = 0, 0

    p_len = len(problems)

    for i in range(p_len):
        if problems[i][0] > mx_alp:
            mx_alp = problems[i][0]

        if problems[i][1] > mx_cop:
            mx_cop = problems[i][1]
    alp = min(alp, mx_alp)
    cop = min(cop, mx_cop)

    dp = [[INF] * (mx_cop + 1) for _ in range(mx_alp + 1)]
    dp[alp][cop] = 0

    for n_alp in range(alp, mx_alp + 1):
        for n_cop in range(cop, mx_cop + 1):
            if n_alp != mx_alp:
                dp[n_alp + 1][n_cop] = min(dp[n_alp][n_cop] + 1, dp[n_alp + 1][n_cop])
            if n_cop != mx_cop:
                dp[n_alp][n_cop + 1] = min(dp[n_alp][n_cop] + 1, dp[n_alp][n_cop + 1])

            for a, b, c, d, cost in problems:
                if a <= n_alp and b <= n_cop:
                    after_alp = min(mx_alp, n_alp + c)
                    after_cop = min(mx_cop, n_cop + d)

                    dp[after_alp][after_cop] = min(dp[after_alp][after_cop], 
                                                   dp[n_alp][n_cop] + cost)
    return dp[-1][-1]