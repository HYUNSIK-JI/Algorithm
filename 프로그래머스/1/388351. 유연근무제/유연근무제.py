def back_startdays(n):
    return 1 if n >= 7 else n + 1

def to_minutes(hhmm):
    return (hhmm // 100) * 60 + (hhmm % 100)

def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        is_check = True
        startdays = startday
        
        limit_min = to_minutes(schedules[i]) + 10
        
        for timelog in timelogs[i]:
            if startdays >= 6:
                startdays = back_startdays(startdays)
                continue
            if to_minutes(timelog) > limit_min:
                is_check = False
                break
            startdays = back_startdays(startdays)
        if is_check:
            answer += 1
        
    return answer
            
            