def solution(food):
    answer = '0'
    for i in range(len(food) - 1, -1, -1):
        while food[i] > 1:
            answer = str(i) + answer
            answer += str(i)
            food[i] -= 2
    return answer