# [Gold III] 마법사 상어와 파이어스톰 - 20058 

[문제 링크](https://www.acmicpc.net/problem/20058) 

### 성능 요약

메모리: 118296 KB, 시간: 452 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색, 구현, 시뮬레이션

### 제출 일자

2024년 9월 17일 15:41:12

### 문제 설명

<p>마법사 상어는 <a href="/problem/20056">파이어볼</a>과 <a href="/problem/20057">토네이도</a>를 조합해 파이어스톰을 시전할 수 있다. 오늘은 파이어스톰을 크기가 2<sup>N</sup> × 2<sup>N</sup>인 격자로 나누어진 얼음판에서 연습하려고 한다. 위치 (r, c)는 격자의 r행 c열을 의미하고, A[r][c]는 (r, c)에 있는 얼음의 양을 의미한다. A[r][c]가 0인 경우 얼음이 없는 것이다.</p>

<p>파이어스톰을 시전하려면 시전할 때마다 단계 L을 결정해야 한다. 파이어스톰은 먼저 격자를 2<sup>L</sup> × 2<sup>L</sup> 크기의 부분 격자로 나눈다. 그 후, 모든 부분 격자를 시계 방향으로 90도 회전시킨다. 이후 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다. (r, c)와 인접한 칸은 (r-1, c), (r+1, c), (r, c-1), (r, c+1)이다. 아래 그림의 칸에 적힌 정수는 칸을 구분하기 위해 적은 정수이다.</p>

<table class="table table-bordered td-center td-middle" style="width:100%;">
	<tbody>
		<tr>
			<td><img alt="" src="https://upload.acmicpc.net/68137f5d-fdbd-48c6-92f0-0a74ee53b0c2/-/preview/" style="width: 300px; height: 302px;"></td>
			<td><img alt="" src="https://upload.acmicpc.net/4216e4de-a9f7-4bf0-9385-e20c583c1228/-/preview/" style="width: 300px; height: 302px;"></td>
			<td><img alt="" src="https://upload.acmicpc.net/a58a4219-afc7-4f77-a194-a5495882eeb4/-/preview/" style="width: 300px; height: 300px;"></td>
		</tr>
		<tr>
			<td>마법을 시전하기 전</td>
			<td>L = 1</td>
			<td>L = 2</td>
		</tr>
	</tbody>
</table>

<p>마법사 상어는 파이어스톰을 총 Q번 시전하려고 한다. 모든 파이어스톰을 시전한 후, 다음 2가지를 구해보자.</p>

<ol>
	<li>남아있는 얼음 A[r][c]의 합</li>
	<li>남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수</li>
</ol>

<p>얼음이 있는 칸이 얼음이 있는 칸과 인접해 있으면, 두 칸을 연결되어 있다고 한다. 덩어리는 연결된 칸의 집합이다.</p>

### 입력 

 <p>첫째 줄에 N과 Q가 주어진다. 둘째 줄부터 2<sup>N</sup>개의 줄에는 격자의 각 칸에 있는 얼음의 양이 주어진다. r번째 줄에서 c번째 주어지는 정수는 A[r][c] 이다.</p>

<p>마지막 줄에는 마법사 상어가 시전한 단계 L<sub>1</sub>, L<sub>2</sub>, ..., L<sub>Q</sub>가 순서대로 주어진다.</p>

### 출력 

 <p>첫째 줄에 남아있는 얼음 A[r][c]의 합을 출력하고, 둘째 줄에 가장 큰 덩어리가 차지하는 칸의 개수를 출력한다. 단, 덩어리가 없으면 0을 출력한다.</p>

