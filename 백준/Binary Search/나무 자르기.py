import sys

#입력 시간을 줄이기 위함
input = sys.stdin.readline

#나무의 수 와 집으로 가져가려는 나무의 길이
n, m = map(int, input().split())

#나무의 높이 리스트로 받기
trees = list(map(int, input().split()))

#이분탐색 0,젤 높은 나무로 설정
start, end = 0, max(trees)

while start <= end:
	# 이분 탐색을 위한 조치
	mid = (start + end) // 2

	#합
	hap = 0

	for tree in trees:
		# 나무의 높이가 중앙값보다 높으면
		if tree > mid:
			# 짜른다.
			hap += (tree - mid)
	# 만약 hap이 가져가려는 나무의 길이 보다 많으면
	if hap >= m:
		# 스타트 부분을 mid + 1 늘려 mid의 기준치를 높임
		start = mid + 1
	else:
		end = mid -1
print(end)