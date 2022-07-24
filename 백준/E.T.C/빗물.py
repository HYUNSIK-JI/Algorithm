import sys

input = sys.stdin.readline


h, w = map(int, input().split())
blocks = list(map(int, input().split()))

answer = 0
for i in range(1, w - 1):
	# 본인을 제외한 좌우에 큰값을 찾기
	left_mx = max(blocks[:i])
	right_mx = max(blocks[i + 1:])

	# 좌우 큰 값은 작은값 찾기
	mn = min(left_mx, right_mx)

	# 만약 본인이 좌우 큰값 중 작은값보다 작으면 빗물이 고인다.
	if blocks[i] < mn:
		# 좌우 큰 값중 작은값 - 본인값 만큼 빗물이 고임
		answer += mn - blocks[i]
#답
print(answer)