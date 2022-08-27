import sys

input = sys.stdin.readline

def back(k, hap):
    global mn
    global mx

    if k == n - 1:
        mx = max(mx, hap)
        mn = min(mn, hap)
        return
    r = hap
    if oper[0] > 0:
        oper[0] -= 1
        back(k + 1, hap + nums[k + 1])
        oper[0] += 1

    if oper[1] > 0:
        oper[1] -= 1
        back(k + 1, hap - nums[k + 1])
        oper[1] += 1

    if oper[2] > 0:
        oper[2] -= 1
        back(k + 1, hap * nums[k + 1])
        oper[2] += 1

    if oper[3] > 0:
        oper[3] -= 1
        if hap < 0:
            back(k + 1, abs(hap) // nums[k + 1] * (-1))
        else:
            back(k + 1, hap // nums[k + 1])
        oper[3] += 1
    hap = r
n = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))

mn = int(1e9)
mx = int(-1e9)

back(0, nums[0])
print(mx)
print(mn)