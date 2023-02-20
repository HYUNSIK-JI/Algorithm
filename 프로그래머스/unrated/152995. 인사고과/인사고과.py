def solution(scores):
    h_x, h_y, h_hap = scores[0][0], scores[0][1], scores[0][0] + scores[0][1]
    scores.sort(key = lambda x: (-x[0], x[1]))
    
    ans = 0
    
    k = 0
    for i in scores:
        if h_x < i[0] and h_y < i[1]:
            return -1
        if k <= i[1]:
            if h_hap < sum(i):
                ans += 1
            k = i[1]
    return ans + 1