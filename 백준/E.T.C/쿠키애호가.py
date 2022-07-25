import sys

input = sys.stdin.readline

for test_case in range(int(input())):
    n, c = map(int, input().split())

    # 현재 갖고 있는 쿠키가 하루에 먹을수 있는 양으로 나눌 때 딱 나누어 떨어지냐 아니냐
    if not n % c:
        print(n // c)
    else:
        print(n // c + 1)