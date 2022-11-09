import sys
input = sys.stdin.readline

photos = int(input())
vote = int(input())

nums = list(map(int, input().split()))

picture = []

for k, i in enumerate(nums):
    for a in range(len(picture)):
        if picture[a][2] == i:
            picture[a][0] += 1
            break
    else:
        if len(picture) == photos:
            picture.sort(key=lambda x: (x[0], x[1]))
            picture.pop(0)
        picture.append([1, k, i])
picture.sort(key=lambda x: (x[2]))
for i in picture:
    print(i[2], end=" ")