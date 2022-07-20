import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    result = []

    while scoville:
        if scoville[0] >= K and not result:
            return answer
        result.append(heapq.heappop(scoville))

        if len(result) == 2:
            heapq.heappush(scoville, result[0] + result[1] * 2)
            answer += 1
            result = []
    return -1