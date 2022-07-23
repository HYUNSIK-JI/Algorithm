import sys

input = sys.stdin.readline

def search(i, target):
    # 자기 자신의 인덱스를 제외하고 만든 리스트 구간
    section = lst[:i] + lst[i + 1:]

    # 투 포인터의 위치
    left = 0
    # 자기자신을 제외한 마지막 인덱스 값은 n - 2
    right = n - 2

    # 투 포인터 시작
    while left < right:
        hap = section[left] + section[right]

        # 우리가 찾던 타켓 즉 좋은 수 인지 아닌지 판별 할려고 하는 값 보다 hap 더 크면 right -= 1
        if target < hap:
            right -= 1
        # 16줄에 반대 되는 상황 hap 더 작으면 left += 1
        elif target > hap:
            left += 1
        # 찾던 타켓 이면
        else:
            # True
            return True
    return False

def check():
    cnt = 0 # 좋은 수의 개수를 카운트 하기 위한 변수
    for i in range(n):
        # 인덱스 와 인덱스 에 해당 되는 값
        if search(i, lst[i]):
            # True 면 좋은 수 이므로 카운트
            cnt += 1
    # 좋은 수의 총 개수
    print(cnt)
    return
# 수의 개수
n = int(input())

# 각각의 수를 나타낸 리스트
lst = sorted(list(map(int, input().split())))
# 각각의 수 하나 하나 체크 하기 위한 함수
check()