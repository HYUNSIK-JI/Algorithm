def solution(k, m, score):
    score.sort(reverse=True)
    ans = 0
    for i in range(0, len(score), m):
        k = score[i: i + m]
        if len(k) == m:
            mn = min(k)
            ans += mn * m
    return ans