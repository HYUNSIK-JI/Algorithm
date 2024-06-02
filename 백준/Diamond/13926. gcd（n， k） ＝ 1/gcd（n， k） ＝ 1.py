import sys
import random
from itertools import combinations


def g(x, n):
    return ((x * x) + 1) % n

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def powmod(a, b, m):
    result = 1
    while b > 0:
        if b % 2 != 0:
            result = (result * a) % m
        b //= 2
        a = (a * a) % m
    return result

def miller_rabin(n):
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

    for _ in range(20):
        a = random.randint(2, n - 1)
        x = powmod(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = powmod(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def pola(n, x):
    p = x
    if miller_rabin(n):
        return n
    else:
        for i in range(2, min(n, 1000)):
            if n % i == 0:
                return i
        y = x
        d = 1
        while d == 1:
            x = g(x, n)
            y = g(g(y, n), n)
            d = gcd(abs(x - y), n)
        if d == n:
            return pola(n, p + 1)
        else:
            if miller_rabin(d):
                return d
            else:
                return pola(d, 2)


def main():
    n = int(input())
    eulers_totient = n

    ans = []
    while n != 1:
        k = pola(n, 2)
        ans.append(int(k))
        n = n // k

    check_sum = eulers_totient
    ans = list(set(ans))
    for i in range(1, len(ans) + 1):
        for t in combinations(ans, i):
            k = 1
            for p in t:
                k *= p
            if i % 2 == 1:
                check_sum -= (eulers_totient // k)
            else:
                check_sum += (eulers_totient // k)

    if eulers_totient == 1:
        print(1)
    else:
        print(check_sum)

if __name__ == "__main__":
    main()
