from heapq import heappush, heappushpop

def solution(n, k, enemy):
    heap = []
    total = 0
    rounds = 0
    
    for i in enemy:
        total += i
        
        if total <= n:
            heappush(heap, -i)
            rounds += 1
        elif k:
            k -= 1
            total += heappushpop(heap, -i)
            rounds += 1
        else:
            break
    return rounds