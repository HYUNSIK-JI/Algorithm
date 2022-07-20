import sys

# 입력 시간을 줄이기 위한 것
input = sys.stdin.readline

# 사람의 수
n = int(input())

# 시간을 최소화 하기 위해 시간들을 오름차순 으로 정렬
times = sorted(list(map(int,input().split())))

# 답을 위한 변수
answer = 0

for i in range(n):
    # 사람 별 기다리는 시간 + 돈을 다 뽑을때 까지의 시간 계산
    hap = sum(times[:i + 1])
    # 사람 마다 총 시간을 합산
    answer += hap
# 답
print(answer)