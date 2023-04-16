def solution(sequence, k):
    # sequence의 길이
    sequence_length = len(sequence)
    
    # 총합
    hap = 0
    
    # index
    end = 0
    
    answer = []
    for index in range(sequence_length):
        while hap < k and end < sequence_length:
            hap += sequence[end]
            end += 1
        
        if hap == k:
            last_index = end - 1
            
            answer.append([index, last_index, last_index - index])
        hap -= sequence[index]
    answer.sort(key=lambda x:x[2])
    return answer[0][0:2]