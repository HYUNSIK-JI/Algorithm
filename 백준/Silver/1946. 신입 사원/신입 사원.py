import sys

for test_case in range(int(sys.stdin.readline())):
	number = int(sys.stdin.readline())
	volunteer = []
	cnt = 0

	for i in range(number):
		a, b = map(int,sys.stdin.readline().split())
		volunteer.append([a,b])

	volunteer.sort(key=lambda x:(x[0]))
	mn = volunteer[0][1]

	for i in volunteer:
		if i[1] <= mn:
			mn = i[1]
			cnt += 1
	print(cnt)