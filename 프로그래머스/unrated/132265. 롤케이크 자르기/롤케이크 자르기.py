def solution(topping):
    answer = 0
    a = {}
    b = set()
    for i in topping:
        a[i] = a.get(i, 0) + 1
    for i in topping:
        a[i] -= 1
        b.add(i)
        if not a[i]:
            del a[i]
        if len(a) == len(b):
            answer += 1
    return answer