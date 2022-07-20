import sys

input = sys.stdin.readline

#좌표의 수
n = int(input())

# x , y 좌표 들을 담기 위한 리스트
position = []

for _ in range(n):
    #x,y 좌표 입력
    x,y = map(int, input().split())
    position.append((x,y))

#x좌표가 증가 순,y좌표 증가순
position.sort(key=lambda x:(x[0],x[1]))

for x,y in position:
    print(x,y)