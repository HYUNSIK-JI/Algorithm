import sys

input = sys.stdin.readline

def back(start):
    if len(answer) > m:
        return
    if len(answer) == m:
        print(*answer)
        return
    for i in range(start, n + 1):
        if i not in answer:
            answer.append(i)
            # 리스트에 넣어줄 자연수의 기준점
            back(i)
            answer.pop()
n, m = map(int, input().split())

answer = []

back(1)