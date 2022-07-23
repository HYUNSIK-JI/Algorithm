import sys

input = sys.stdin.readline

def back(start):
    # 길이가 m 초과시 함수 종료
    if len(answer) > m:
        return
    # 길이가 m 이면 리스트 내용을 보여주고 함수 종료
    if len(answer) == m:
        print(*answer)
        return
    #start 변수 로 for 스타트를 지정
    for i in range(start, n + 1):
        answer.append(i)
        back(i)
        answer.pop()

n, m = map(int,input().split())
answer = []
back(1)