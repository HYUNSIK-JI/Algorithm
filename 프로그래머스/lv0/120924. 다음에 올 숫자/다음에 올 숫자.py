def solution(common):
    answer = 0
    ans = {}
    for i in range(len(common) - 1):
        k = common[i + 1] - common[i]
        ans[k] = ans.get(k, 0) + 1
    if len(ans) == 1:
        answer = common[-1]
        for i in ans.keys():
            answer = common[-1] + i
    else:
        k = common[-1] // common[-2]
        answer = common[-1] * k
    return answer