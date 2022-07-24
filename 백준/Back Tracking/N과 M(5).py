import sys

input = sys.stdin.readline

def back():
	if len(answer) > m:
		return
	if len(answer) == m:
		print(*answer)
		return
	for i in range(n):
		# 동일한 숫자가 들어 가게 하지 않기 위함
		if lst[i] not in answer:
			answer.append(lst[i])
			back()
			answer.pop()
n, m = map(int, input().split())

#출력문과 동일하게 나오게하기 위한 오름차순 정렬
lst = sorted(list(map(int, input().split())))

answer = []

back()