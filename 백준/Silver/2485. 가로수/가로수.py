import sys

input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_gcd_of_list(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = gcd(result, num)
    return result

n = int(input())

existing = [int(input()) for _ in range(n)]
existing_interval = [existing[i + 1] - existing[i] for i in range(n - 1)]

interval = find_gcd_of_list(existing_interval)

required_trees = sum([(gap // interval) - 1 for gap in existing_interval])

print(required_trees)
