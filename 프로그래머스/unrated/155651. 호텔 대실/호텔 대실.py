from heapq import heappush, heappop

def solution(book_time):
    book_time.sort(key=lambda x:(x[0]))
    room = []
    ans = 0
    
    for s, e in book_time:
        s = s.replace(":","")
        e = e.replace(":","")
        
        s = int(s[:2]) * 60 + int(s[2:])
        e = int(e[:2]) * 60 + int(e[2:])
        
        while room and room[0] + 10 <= s:
            heappop(room)
        heappush(room, e)
        ans = max(ans, len(room))
    return ans

    