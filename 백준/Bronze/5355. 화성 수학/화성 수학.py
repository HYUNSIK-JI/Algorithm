import sys
input = sys.stdin.readline

def cal(a, equation):
    for b in equation:
        if b == "@":
            a *= 3
        elif b == "%":
            a += 5
        else:  # "#"
            a -= 7
    return a

ans = []

for _ in range(int(input())):
    m_q = input().split()
    num = float(m_q[0])
    ans.append(f"{cal(num, m_q[1:]):.2f}")

print(*ans, sep="\n")
