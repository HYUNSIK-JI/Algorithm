import sys

input = sys.stdin.readline

def back(start):
	for i in range(1,(start//2) + 1):
		if answer[-i:] == answer[-2 * i: -i]:
			return -1
	if start == n:
		print("".join(map(str,answer)))
		return 0
	for i in range(1,4):
		answer.append(i)
		if back(start + 1) == 0:
			return 0
		answer.pop()
n = int(input())
answer = []
mn = []
back(0)