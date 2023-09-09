# [Platinum V] 전봇대 - 8986 

[문제 링크](https://www.acmicpc.net/problem/8986) 

### 성능 요약

메모리: 115160 KB, 시간: 128 ms

### 분류

삼분 탐색

### 문제 설명

<p>일직선상에 N개의 전봇대가 한 줄로 서있다. 편의상, 일직선을 x-축이라 하고, 전봇대가 서 있는 위치 x<sub>0</sub>, x<sub>1</sub>, ..., x<sub>N-1</sub>은 x-축 상의 x-좌표라고 하자. x<sub>0</sub>는 항상 0이고 x<sub>i</sub>(i ≥ 1)는 양의 정수라고 가정한다.</p>

<p>이 전봇대들을 이웃한 두 전봇대 사이의 거리가 모두 일정하도록 일부 전봇대들을 옮기려고 한다. 이때 이동해야하는 전봇대들의 거리의 합이 최소가 되도록 해야 한다. 단, x<sub>0</sub>에 위치한 전봇대는 움직일 수 없고, 이동하는 전봇대들은 정수 좌표 위치로만 이동 가능하다. </p>

<p>예를 들어, 아래의 그림 1과 같이 전봇대가 주어져 있다고 하자.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/a002346d-e308-48b5-9245-448072550c4b/-/preview/" style="width: 262px; height: 37px;"></p>

<p style="text-align: center;">그림 1. 전봇대의 위치</p>

<p>이 경우 그림 2에서와 같이 x-좌표 6과 9에 위치한 전봇대를 각각 x-좌표 8과 12인 곳으로 이동하면, 모든 이웃한 전봇대들의 거리는 4로 같고 전봇대의 이동 거리의 합은 5이다. </p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/dc3c0cc4-44e5-4388-b020-19f2dc895ee2/-/preview/" style="width: 262px; height: 33px;"></p>

<p style="text-align: center;">그림 2. 전봇대의 이동 예 1</p>

<p>하지만 그림 3과 같이 x-좌표 4에 위치한 전봇대만을 x-좌표 3인 곳으로 이동하면, 이웃한 전봇대들의 거리는 모두 3이고 전봇대의 이동 거리의 합은 1이다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/6b05f83c-8acc-4408-927e-9055afa11ee1/-/preview/" style="width: 262px; height: 33px;"></p>

<p style="text-align: center;">그림 3. 전봇대 이동의 예 2</p>

<p>전봇대들의 위치 x<sub>0</sub>, x<sub>1</sub>, ..., x<sub>N-1</sub>이 주어지면, 모든 이웃한 전봇대들의 거리가 같도록 전봇대들을 이동할 때(x<sub>0</sub>에 위치한 전봇대는 고정), 이동 거리의 합이 최소가 되도록 하는 프로그램을 작성하시오.</p>

### 입력 

 <p>입력의 첫 줄은 전봇대의 수 N (1 ≤ N ≤ 100,000)이 주어진다. 두 번째 줄에는 전봇대의 위치를 나타내는 N개의 서로 다른 x-좌표 x<sub>i</sub>(i = 0, ..., N-1)가 빈칸을 사이에 두고 오름차순으로 주어진다. x<sub>i</sub>는 정수이고, i=0일 때 x<sub>i</sub>=0, 그 외에는 1 ≤ x<sub>i</sub> ≤ 1,000,000,000 이다.</p>

### 출력 

 <p>출력은 단 한 줄이며, 모든 이웃한 전봇대들의 거리가 같도록 전봇대들의 이동거리 합의 최솟값을 출력한다.</p>

