import sys

input = sys.stdin.readline

#카드의 개수 와 카드의 합
n, m = map(int, input().split())

#카드들
cards = list(map(int, input().split()))

#카드들의 합들을 저장 할 리스트할당
answer = []

#중복으로 더 할 수 없으므로 y = x + 1 ,z = y + 1
for x in range(1, n):
    for y in range(x + 1, n):
        for z in range(y + 1, n):
            #카드들의 합
            hap = cards[x] + cards[y] + cards[z]

            #카드들의 합들이 m보다 작거나 같으면
            if hap <= m:
                #answer리스트에 추가
                answer.append(hap)
# 가장 큰수 보여줘
print(max(answer))