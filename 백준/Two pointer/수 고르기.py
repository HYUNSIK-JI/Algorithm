import sys

input = sys.stdin.readline

# 숫자의 개수,차이 값
n, m = map(int, input().split())

# numbers 라는 리스트에 정수들을 집어넣고 오름차순으로 정렬
numbers = sorted([int(input()) for _ in range(n)])

# 정수의 범위가 0~10억 이므로 10억보다 큰 값으로 정의
mn = 2e9

#투포인터 위치
left, right = 0, 1

while left <= right and right < n:
    #hap = 두 정수의 차이값
    hap = numbers[right] - numbers[left]

    # 만약 두 정수의 차이값이 기준치의 m보다 작으면
    if hap < m:
        # right 포인터 위치를 하나 증가
        right += 1
    # 21줄 내용의 반대라면
    else:
        # 두 정수의 차이가 최솟값 보다 작으면
        if hap < mn:
            # 최솟값을 다시 정의
            mn = hap
        # left 포인터 위치를 하나 증가
        left += 1
#정답
print(mn)