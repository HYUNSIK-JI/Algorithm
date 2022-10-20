def solution(dirs):
    position = set()
    dic = {"U":(0, 1), "D":(0, -1), "L":(-1, 0), "R":(1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx = x + dic[i][0]
        ny = y + dic[i][1]
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            position.add((x, y, nx, ny))
            position.add((nx, ny, x, y))
            x, y = nx, ny
    return len(position)//2