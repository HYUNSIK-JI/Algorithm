import sys

input = sys.stdin.readline

def solve_mask(ingredients):
    n = len(ingredients)
    ans = int(1e9)

    for mask in range(1, 1 << n):
        sour = 1
        bitter = 0
        for i in range(n):
            if mask & (1 << i):
                s, b = ingredients[i]
                sour *= s
                bitter += b
        ans = min(ans, abs(sour - bitter))
    return ans

gre = [tuple(map(int, input().split())) for _ in range(int(input()))]

print(solve_mask(gre))