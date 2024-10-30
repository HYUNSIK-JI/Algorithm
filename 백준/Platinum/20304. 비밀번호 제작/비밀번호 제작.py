import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def hamming_distance(x, y):
    return bin(x ^ y).count('1')

N = int(input())
M = int(input())
attempted_passwords = list(map(int, input().split()))

visited = set(attempted_passwords)
queue = deque([(pw, 0) for pw in attempted_passwords])
max_safety = 0

while queue:
    current_pw, dist = queue.popleft()
    max_safety = max(max_safety, dist)
    
    for i in range(N.bit_length() + 1):
        candidate_pw = current_pw ^ (1 << i)
        if 0 <= candidate_pw <= N and candidate_pw not in visited:
            visited.add(candidate_pw)
            queue.append((candidate_pw, dist + 1))

print(max_safety)