import sys

input = sys.stdin.readline

def find_f(x):
    result = 0

    for i in range(n):
        result += abs(x_positon[i] - x * i)
    return result

n = int(input())

x_positon = list(map(int, input().split()))

start = 1
end = int(1e9)


while end - start >= 3:
    mid_one = (start * 2 + end) // 3
    mid_two = (start + end * 2) // 3


    if find_f(mid_one) < find_f(mid_two):
        end = mid_two
    else:
        start = mid_one

answer = 1e9

for i in range(start, end + 1):
    answer = min(answer, find_f(i))

print(answer)