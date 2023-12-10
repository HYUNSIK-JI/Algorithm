def solution(dot):
    x = dot[0]
    y = dot[1]
    
    if x > 0 and y > 0:
        return 1
    elif x > 0 and y < 0:
        return 4
    elif x < 0 and y > 0:
        return 2
    else:
        return 3