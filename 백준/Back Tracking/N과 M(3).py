import sys

input = sys.stdin.readline

def back():
    # 길이가 m이 넘어가면 함수 종료
    if len(numbers) > m:
        return
    # 길이가 m이면 리스트를 보여주고 함수 종료
    if len(numbers) == m:
        print(*numbers)
        return
    # 1~n 까지
    for i in range(1, n + 1):
        # 중복이 포함으로 numbers에 i값을 넣고 다시 함수 시작
        numbers.append(i)
        back()
        # 함수가 끝나고 다시 본래 함수 로 돌아 왔을 때는 가장 최근 값 빼기
        numbers.pop()
n, m = map(int, input().split())
numbers = []
back()