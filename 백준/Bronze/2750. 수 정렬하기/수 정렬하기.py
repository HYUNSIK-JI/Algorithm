import sys
input = sys.stdin.readline

number_list = [int(input()) for _ in range(int(input()))]
print(*sorted(number_list), sep="\n")
