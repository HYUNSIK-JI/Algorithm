def make_common_score(a, b, c, n):
    total = 1
    for i in range(1, n + 1):
        total *= (a ** i + b ** i + c ** i)
    return total

def solution(a, b, c):
    if a == b == c:
        return make_common_score(a, b, c, 3)
    elif a != c and a != b and b != c:
        return make_common_score(a, b, c, 1)
    return make_common_score(a, b, c, 2)
    