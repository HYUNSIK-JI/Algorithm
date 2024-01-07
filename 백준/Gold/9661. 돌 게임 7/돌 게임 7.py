import sys

input = sys.stdin.readline

n = int(input())

answer = ['CY', 'SK', 'CY', 'SK', 'SK', 'SK']

print(answer[n % 5])