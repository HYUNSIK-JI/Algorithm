import sys

#입력 시간을 줄이기 위함
input = sys.stdin.readline

#n의 값을 내림차순 정렬을 위해 list화
n = list(input().rstrip())

#내림차순 정렬
n.sort(reverse = True)

#내림차순 되었는지 확인
# print(n)

#join함수를 이용해 숫자들 끼리 공백 제거
print("".join(n))