def solution(park, routes):
    n = len(park)
    m = len(park[0])
    x, y = 0, 0
    r = {"E": (0, 1), "W": (0, -1), "N": (-1, 0), "S": (1, 0)}
    maps = [["0"] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if park[i][j] == "S":
                x, y = i, j
            maps[i][j] = park[i][j]
    
    for i in routes:
        k = i.split(" ")
        dir = k[0]
        num = int(k[1])
        
        dx = r[dir][0]
        dy = r[dir][1]
        cnt = 0
        check = True
        while num:
            num -= 1
            if 0 <= x + dx < n and 0 <= y + dy < m:
                if maps[x + dx][y + dy] != "X":
                    x += dx
                    y += dy
                    cnt += 1
                else:
                    check = False
                    break
            else:
                check = False
                break
        if not check:
            for _ in range(cnt):
                x -= dx
                y -= dy
    return [x, y]
            
        