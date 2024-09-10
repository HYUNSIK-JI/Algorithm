def solution(a, d, included):
    total = 0
    for k, v in enumerate(included):
        if v:
            total += a + (d * k)
    return total