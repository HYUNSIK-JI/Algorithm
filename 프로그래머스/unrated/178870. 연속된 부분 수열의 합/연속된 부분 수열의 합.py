def solution(sequence, k):
    start = 0
    end = 0
    sequence_sum = sequence[0]
    
    answer = []
    
    while start <= end and end < len(sequence):
        if sequence_sum < k:
            end += 1
            if end < len(sequence):
                sequence_sum += sequence[end]
        elif sequence_sum > k:
            sequence_sum -= sequence[start]
            start += 1
        else:
            answer.append([start, end, end - start])
            sequence_sum -= sequence[start]
            start += 1
    
    answer.sort(key=lambda x: x[2])
    return answer[0][0:2]
