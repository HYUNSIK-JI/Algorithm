import sys

input = sys.stdin.readline

#지방의 수
n = int(input())

#지방마다 예산요청 금액
prices = list(map(int, input().split()))

#총 예산
m = int(input())

#이분탐색을 위한 기초작업
start, end = 1, max(prices)

while start <= end:
	# 평균값
	mid = (start + end) // 2
	hap = 0

	for price in prices:
		if price < mid:
			# 평균값 보다 예산값이 작으면 hap에 예산값을 더하기
			hap += price
		else:
			# 평균값 보다 예산값이 많으면 hap에 평균값을 더하기
			hap += mid
	#총 금액이 예산값 보다 작으면 예산값을 최대로 쓰기 위해 start = mid + 1 을 진행
	if hap <= m:
		start = mid + 1
	#총 예산값 보다 덜 쓰기 위해 end = mid -1 진행
	else:
		end = mid -1
#출력
print(end)