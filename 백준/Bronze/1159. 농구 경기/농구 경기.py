from collections import defaultdict
import sys

input = sys.stdin.readline
_dict = defaultdict(int)

for _ in range(int(input())):
    _dict[input().rstrip()[0]] += 1

ans = sorted([k for k, v in _dict.items() if v >= 5])
print("".join(ans) if ans else "PREDAJA")
