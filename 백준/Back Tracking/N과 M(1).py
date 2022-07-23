import sys

input = sys.stdin.readline

def back():
    # 만약 길이가 m이 넘어가면 함수 종료
    if len(answer) > m:
        return
    # 만약 길이가 m이면 해당 리스트 를 보여주고 함수 종료
    if len(answer) == m:
        print(*answer)
        return
    # 1 ~ n + 1
    for i in range(1, n + 1):
        #중복이 포함안되므로 없는 것만 넣어야 한다.
        if i not in answer:
            answer.append(i)
            back()
            answer.pop()
#자연수 의 범위 와 수열의 길이
n, m = map(int, input().split())

# 자연수 들을 넣을 리스트
answer = []

# 백트래킹 함수
back()