import sys

input = sys.stdin.readline

_str = ''

for _ in range(3):
    _str += input().rstrip()

print(eval(_str))