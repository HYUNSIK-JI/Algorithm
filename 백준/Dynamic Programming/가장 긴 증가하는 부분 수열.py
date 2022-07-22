import sys

input = sys.stdin.readline

# 수열의 크기
N = int(input())

# 리스트 선언
lst = list(map(int, input().split()))

# N개 길이 만큼 리스트 1로 선언 1로 선언하는 이유는 모든 부분 수열은 본인 혼자만 들어가 있을수도 있기때문에 1로 선언
DP = [1] * N

for i in range(N):
    for j in range(0,i + 1):
        # 본인차례 이전 에 모든 숫자 들을 비교
        if lst[i] > lst[j]:
            # 기존의 길이 즉 이미 포함된 숫자들을 포함 시키지 않기 위해 max 메서드를 통해 길이 비교
            DP[i] = max(DP[i], DP[j] + 1)
print(max(DP))