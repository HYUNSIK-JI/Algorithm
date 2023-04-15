def solution(players, callings):
    players_name = {}
    reverse_player_name = {}
    
    for player_index, player in enumerate(players):
        players_name[player] = player_index
        reverse_player_name[player_index] = player
        
    for calling in callings:
        if calling in players_name.keys():
            
            # 딕셔너리 value로 name를 찾기 위한 데이터
            # 이름이 불린 선수의 순위
            calling_data = players_name.get(calling)
            # 이름이 불린 선수 보다 앞선 선수 순위
            pre_calling_data = calling_data - 1
            
            # name 찾기
            # 이름이 불린 선수 보다 앞선 순위의 선수
            pre_name = reverse_player_name.get(pre_calling_data)
            # 이름이 불린 선수의 이름
            name = reverse_player_name.get(calling_data)
            
            players_name[name] = pre_calling_data
            players_name[pre_name] = calling_data
            
            reverse_player_name[pre_calling_data] = name
            reverse_player_name[calling_data] = pre_name
    # value 으로 딕셔너리 정렬
    players_name = sorted(players_name.items(), key=lambda x: x[1])
    
    # 정답
    answer = []
    
    for name, rank in players_name:
        answer.append(name)
    return answer