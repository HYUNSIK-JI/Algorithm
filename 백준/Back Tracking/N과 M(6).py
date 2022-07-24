import sys

input = sys.stdin.readline

def back(start):
	# answer의 길이가 m일때
	if len(answer) == m:
		#print
		print(*answer)
		return
	for i in range(start, n):
		#중복 제거
		if lst[i] not in answer:
			answer.append(lst[i])
			back(i)
			answer.pop()

#자연수의 개수, 수열의 길이
n, m = map(int, input().split())

#수열 입력 -> 오름차순
lst = sorted(list(map(int, input().split())))

answer = []

#combination
back(0)