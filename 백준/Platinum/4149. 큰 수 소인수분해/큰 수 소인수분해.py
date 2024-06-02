import sys
import random
from math import gcd

input = sys.stdin.readline

def miller_rabin(n, k):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if not n % 2:
        return False

    r, d = 0, n - 1
    while not d % 2:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def pollards_rho(n):
    if not n % 2:
        return 2
    x = random.randint(2, n-1)
    y = x
    c = random.randint(1, n-1)
    d = 1

    while d == 1:
        x = (pow(x, 2, n) + c + n) % n
        y = (pow(y, 2, n) + c + n) % n
        y = (pow(y, 2, n) + c + n) % n
        d = gcd(abs(x - y), n)
        if d == n:
            return pollards_rho(n)
    return d

def find_factors(n):
    if n == 1:
        return []
    if miller_rabin(n, 5):
        return [n]

    factor = pollards_rho(n)
    factors = find_factors(factor) + find_factors(n // factor)
    return factors

if __name__ == "__main__":
    n = int(input())

    factors = find_factors(n)
    factors.sort()
    print(*factors, sep="\n")
