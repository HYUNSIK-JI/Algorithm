def check_health(n):
    return -1 if n < 0 else n

def monster_attack_time(attack_damage, now_health):
    return now_health - attack_damage

def success_health(max_health, now_health, sequence, bandage):
    # 초당 회복
    now_health += bandage[1]
    # 연속 성공 보너스 (sequence가 bandage[0]이 되는 '그 초'에 보너스 적용)
    if sequence == bandage[0]:
        now_health += bandage[2]
        sequence = 0  # 보너스 후 연속 카운트 초기화
    # 체력 상한
    if now_health > max_health:
        now_health = max_health
    return now_health, sequence

def solution(bandage, health, attacks):
    # bandage = [t, x, y]  (t초 연속 성공 시 y 추가 회복, 초당 x 회복)
    now_time = 0
    last_time = attacks[-1][0]

    monster_idx = 0
    sequence = 0
    now_health = health

    while now_time < last_time:
        # 사망 체크
        if check_health(now_health) < 0:
            return -1

        now_time += 1

        # 다음 공격 시간/데미지 (없으면 무한대로)
        if monster_idx < len(attacks):
            attack_time, attack_damage = attacks[monster_idx]
        else:
            attack_time, attack_damage = float('inf'), 0

        if now_time == attack_time:
            # 공격 발생
            now_health = monster_attack_time(attack_damage, now_health)
            sequence = 0
            monster_idx += 1
            # 공격 직후 사망 체크
            if check_health(now_health) < 0:
                return -1
        else:
            # 회복 발생
            sequence += 1
            now_health, sequence = success_health(health, now_health, sequence, bandage)

    return now_health if now_health > 0 else -1
