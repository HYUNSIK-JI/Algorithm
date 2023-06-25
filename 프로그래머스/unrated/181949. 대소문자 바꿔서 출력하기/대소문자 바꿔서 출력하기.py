str = input()
ans = []

for s in str:
    change = ord(s)
    if 65 <= change < 97:
        ans.append(chr(change + 32))
    else:
        ans.append(chr(change - 32))
print("".join(ans))