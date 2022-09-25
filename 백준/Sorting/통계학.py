import sys

input = sys.stdin.readline

n = int(input())
nums = sorted([int(input()) for _ in range(n)])
num = [[0] * 2 for _ in range(4001)]
mx = 0
print(round(sum(nums) / n)) #산술 평균
print(nums[n//2])# 중앙값

for i in nums:
    # 마이너스, 플러스 구분
    if i < 0:
        num[abs(i)][0] += 1 #마이너스 라면 이중리스트에서의 해당 숫자 인덱스로 접근 그리구 그중 앞에부분을[0] +1
    else:
        num[i][1] += 1 # 반대로 플러스면 [1] +1
    mx = max(mx, num[i][0], num[i][1])
c = []
for i in range(4001):
    # 마이너스 부분
    if num[i][0] == mx and num[i][0]:
        c.append(-i)
    # 플러스 부분
    if num[i][1] == mx and num[i][1]:
        c.append(i)
# 정렬
c.sort()
# 한개라면 첫번째
if len(c) == 1:
    print(c[0])
# 두개이상 이라면 두번째꺼
else:
    print(c[1])
# 범위
print(nums[-1] - nums[0])