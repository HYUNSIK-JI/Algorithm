from collections import deque
def solution(picks, minerals):

    answer = 0
    scores = [[1, 1, 1],[5, 1, 1],[25, 5, 1]]
    dig = {
        "diamond":0,
        "iron" : 1,
        "stone" : 2
    }
    info = []
    minerals = minerals[:5 * sum(picks)]
    q = deque(minerals)
    while q:
        k = 0
        Dia, Iron, Stone = 0,0,0
        while k < 5:
            k += 1
            mineral = q.popleft()
            Dia += scores[0][dig[mineral]]
            Iron += scores[1][dig[mineral]]
            Stone += scores[2][dig[mineral]]
            if not q:
                break
        info.append([Dia,Iron,Stone])
    info.sort(key = lambda x : [x[2],x[1],x[0]])

    for idx, p in enumerate(picks):
        for _ in range(p):
            if info:
                answer += info.pop()[idx]
            else:
                return answer

    return answer