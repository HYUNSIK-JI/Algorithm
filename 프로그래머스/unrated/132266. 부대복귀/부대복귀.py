import sys
from heapq import heappush, heappop

INF = sys.maxsize

def solution(n, roads, sources, destination):
    ans = []
    maps = [[] for _ in range(n + 1)]
    
    for a, b in roads:
        maps[a].append((b, 1))
        maps[b].append((a, 1))
    
    q = []
    heappush(q, (0, destination))
    dis = [INF] * (n + 1)
    dis[destination] = 0
    
    while q:
        dist, now = heappop(q)
        
        if dis[now] < dist:
            continue
        
        for i in maps[now]:
            cost = dist + i[1]
            
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heappush(q, (cost, i[0]))
    for i in sources:
        if dis[i] == INF:
            ans.append(-1)
        else:
            ans.append(dis[i])
    return ans