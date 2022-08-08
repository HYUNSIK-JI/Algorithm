for test_case in range(1, int(input()) + 1):
    names = sorted(list(set(input().rstrip() for _ in range(int(input())))), key=lambda x: (len(x), x))
    print(f"#{test_case}", *names, sep="\n")