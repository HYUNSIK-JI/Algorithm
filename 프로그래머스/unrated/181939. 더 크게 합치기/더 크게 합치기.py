def solution(a, b):
    result = max(int("".join([str(a), str(b)])), int("".join([str(b), str(a)])))
    return result