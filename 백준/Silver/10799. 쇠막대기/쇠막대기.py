import sys

sentence=sys.stdin.readline().rstrip()
stack=[]
result=0

for s in range(len(sentence)):
	if sentence[s]=="(":
		stack.append("(")
	else:
		if sentence[s-1]=="(":
			stack.pop()
			result+=len(stack)
		else:
			stack.pop()
			result+=1
print(result)