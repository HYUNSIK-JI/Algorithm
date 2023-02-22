from collections import defaultdict

def solution(weights):
    ans = 0
    r = defaultdict(int)
    for w in weights:
        ans += r[w] + r[w * 2] + r[w / 2] + r[(w * 2) / 3] +r[(w * 3) / 2] +r[(w * 3) / 4] + r[(w * 4) / 3]
        r[w] += 1
    return ans