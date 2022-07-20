import sys

n = int(sys.stdin.readline())
stack = []

for i in range(n):
	command = sys.stdin.readline().split()

	if command[0] == "top":
		if len(stack) == 0:
			print(-1)
		else:
			print(stack[-1])
	if command[0] == "size":
		print(len(stack))

	if command[0] == "empty":
		if len(stack) == 0:
			print(1)
		else:
			print(0)
	if command[0] == "pop":
		if len(stack) != 0:
			a = stack.pop()
			print(a)
		else:
			print(-1)
	if command[0] == "push":
		stack.append((int(command[1])))