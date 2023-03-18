score = {"A+": 45, "A0": 40, "B+": 35, "B0": 30, "C+": 25, "C0": 20, "D+": 15, "D0": 10, "F": 0}
value = {"1.0": 10, "2.0": 20, "3.0": 30, "4.0": 40}
num = 0
ans = 0

for _ in range(20):
    temp = input().split(" ")

    if temp[2] == "P":
        continue
    num += value.get(temp[1])
    ans += value.get(temp[1]) * score.get(temp[2])

print(ans / num / 10)