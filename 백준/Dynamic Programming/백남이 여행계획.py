import sys

input = sys.stdin.readline

n, m = map(int, input().split())

thing = [list(map(int, input().split())) for _ in range(n)] # 각 물건의 무게, 해당 물건의 가치
bag = [list(map(int, input().split())) for _ in range(m)] # 각 가방이 견딜수 있는 무게
num, answer = 0, 0
dp = [[0] * (max(bag) + 1) for _ in range(n + 1)] # max(bag)으로 최대치 까지 리스트 확장

for i in range(1, n + 1):
    for j in range(1, max(bag) + 1):
        w = thing[i - 1][0]
        v = thing[i - 1][1]

        if w > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v) # 12~20 일반적인 냅색문제 베이스 코드

for i in bag:
    p = dp[n][i] / i
    if answer < p:
        answer = p
        num = bag.index(i)
# 22 ~ 26 문제에서 요구하는 효율성 계산
print(num + 1)

풀이
문제를 보자마자 냅색문제인 것을 알 수 있다.

일반적인 냅색문제랑 살짝 다른 점은 가방에 1개가 아닌 M개라서 이중에서 효율이 좋은 가방을 선택하라고 합니다.


하지만 가방 M개를 일일이 돌렸다가 시간초과 와 메모리초과를 맞았다. 다른 방안을 강구하다가 

냅색 알고리즘을 정확하게 이해 하지 못했기 때문에 시간초과 와 메모리초과를 맞았다라고 생각되어

다시 기본적인 냅색알고리즘이 돌아가는 구상도를 백준 12865 평범한 배낭 문제 기준으로 그려보았다.


1) x축엔 가방 1~K 까지의 무게, y축은 물건 N개 개수 만큼의 배열을 만들어준다.

2) 행을 차례대로 돌며 다음과 같은 알고리즘을 수행해준다.

 

3-0) 현재 물건이 현재 돌고있는 무게보다 작다면 바로 [이전 물건][같은 무게] (knapsack[i-1][j]를 입력해준다.

3-1) 현재 물건을 넣어준다. 물건을 넣은 뒤의 남은 무게를 채울 수 있는 최댓값(knapsack[i-1][j-weight]을 위의 행에서 가져와 더해준다.

3-2) 현재 물건을 넣어주는 것보다. 다른 물건들로 채우는 값(knapsack[i-1][j])을 가져온다.

4) 3-1과 3-2 중 더 큰 값을 knapsack[i][j]에 저장해준다. 이 값은 현재까지의 물건들로 구성할 수 있는 가장 가치 높은 구성이다.

5) knapsack[N][K]는 곧, K무게일 때의 최댓값을 가리킨다.

 

수식
결국 수식으로 표현하면 다음과 같다.

knapsack[i][j] = max(현재 물건 가치 + knapsack[이전 물건][현재 가방 무게 - 현재 물건 무게], knapsack[이전 물건][현재 가방 무게])

knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

 

결국 아래와 같은 엑셀이 만들어진다.

        0   1   2   3   4   5   6   7
weight  value                                
6   13      0   0   0   0   0   13  13
4   8       0   0   0   8   8   13  13
3   6       0   0   6   8   8   13  14
5   12      0   0   6   8   12  13  14


분석을 통해서 가방 M개를 일일이 냅색을 돌리지 말고 M개의 가방중에서 가장 용량이 큰 가방을 기준삼아 냅색을 돌리면 된다는 사실을 알아냈다.

이렇게 냅색을 돌렸으면 이제 dp[n][i번째 가방무게]의 값은 물품 N개를 선택적으로 골라 i번째 가방무게에 넣을 수 있는 최대 가치가 된다.