import sys
input = sys.stdin.readline


n = int(input())

_list = list(map(int, input().split()))


if n == 1:
    if _list[0] == 0:
        print("YES")
        print(0)
    else:
        print("YES")
        print(str(_list[-1]) * 3)
else:
    print("YES")
    print(str(_list[-1]) * 3)