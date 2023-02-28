import sys
input = sys.stdin.readline

def back(s, sign, num, k, string):
    if (k == n):
        s = s + (sign * num)
        if not s:
            print(string)
    else:
        back(s, sign, num * 10 + (k + 1), k + 1, string + ' ' + str(k + 1))
        back(s + sign * num, 1, (k + 1), k + 1, string + '+' + str(k + 1))
        back(s + sign * num, -1, (k + 1), k + 1, string + '-' + str(k + 1))

test_case = int(input())

for _ in range(test_case):
    n = int(input())
    back(0, 1, 1, 1, "1")
    print()