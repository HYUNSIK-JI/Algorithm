import sys

input = sys.stdin.readline


def back(n):
    if n == len(zero_postion):
        for row in sudoku:
            print(*row, sep="")
        exit()
    a, b = zero_postion[n]
    x, y = a // 3, b // 3
    numbers2 = numbers[:]

    # 3 * 3 체크
    for i in range(3 * x, 3 * (x + 1)):
        for j in range(3 * y, 3 * (y + 1)):
            if sudoku[i][j] in numbers2:
                numbers2.remove(sudoku[i][j])
    # 가로 및 세로
    for i in range(9):
        if sudoku[a][i] in numbers2:
            numbers2.remove(sudoku[a][i])
        if sudoku[i][b] in numbers2:
            numbers2.remove(sudoku[i][b])

    for i in numbers2:
        sudoku[a][b] = i
        back(n + 1)
    sudoku[a][b] = 0
sudoku = [list(map(int, list(input().rstrip()))) for _ in range(9)]
zero_postion = [(i, j) for i in range(9) for j in range(9) if not sudoku[i][j]]
numbers = [i for i in range(1, 10)]
back(0)
