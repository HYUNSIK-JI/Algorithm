import sys

input = sys.stdin.readline

#랜선의 갯수,필요한 랜선의 갯수
n, k = map(int, input().split())

#각각의 랜선들
lines = [int(input()) for _ in range(n)]

#이분탐색을 위한 기초작업
#start = 0 이 아닌 1로 시작하는 이유는 문제에서 자연수 라고 주어졌다.
start, end = 1, max(lines)

while start <= end:
	# 중앙값
	mid = (start + end) // 2

	#랜선의 갯수을 위한것
	hap = 0

	for line in lines:
		# 만약 중앙값 보다 큰 랜선이라면
		if line >= mid:
			# 중앙값 만큼 짤라서 나온 갯수를 hap에 더하기
			hap += line // mid

	# 짤라서 나온 랜선의 갯수가 필요한 갯수보다 많거나 같으면 중앙값을 더 크게 하기 위한 작업
	if hap >= k:
		start = mid + 1
	else:
		#짤라서 나온 랜선의 갯수가 필요한 갯수보다 적으면 중앙값을 더 작게 하기 위한 작업
		end = mid - 1
#답 출력
print(end)