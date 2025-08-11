# [level 1] [PCCP 기출문제] 1번 / 붕대 감기 - 250137 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/250137) 

### 성능 요약

메모리: 9.24 MB, 시간: 0.90 ms

### 구분

코딩테스트 연습 > PCCP 기출문제

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2025년 08월 11일 18:00:28

### 문제 설명

<p>어떤 게임에는 <code>붕대 감기</code>라는 기술이 있습니다.</p>

<p><code>붕대 감기</code>는 <code>t</code>초 동안 붕대를 감으면서 1초마다 <code>x</code>만큼의 체력을 회복합니다. <code>t</code>초 연속으로 붕대를 감는 데 성공한다면 <code>y</code>만큼의 체력을 추가로 회복합니다. 게임 캐릭터에는 최대 체력이 존재해 현재 체력이 최대 체력보다 커지는 것은 불가능합니다.</p>

<p>기술을 쓰는 도중 몬스터에게 공격을 당하면 기술이 취소되고, 공격을 당하는 순간에는 체력을 회복할 수 없습니다. 몬스터에게 공격당해 기술이 취소당하거나 기술이 끝나면 그 즉시 <code>붕대 감기</code>를 다시 사용하며, 연속 성공 시간이 0으로 초기화됩니다.</p>

<p>몬스터의 공격을 받으면 정해진 피해량만큼 현재 체력이 줄어듭니다. 이때, 현재 체력이 0 이하가 되면 캐릭터가 죽으며 더 이상 체력을 회복할 수 없습니다.</p>

<p>당신은 <code>붕대감기</code> 기술의 정보, 캐릭터가 가진 최대 체력과 몬스터의 공격 패턴이 주어질 때 캐릭터가 끝까지 생존할 수 있는지 궁금합니다.</p>

<p><code>붕대 감기</code> 기술의 시전 시간, 1초당 회복량, 추가 회복량을 담은 1차원 정수 배열 <code>bandage</code>와 최대 체력을 의미하는 정수 <code>health</code>, 몬스터의 공격 시간과 피해량을 담은 2차원 정수 배열 <code>attacks</code>가 매개변수로 주어집니다. 모든 공격이 끝난 직후 남은 체력을 return 하도록 solution 함수를 완성해 주세요. <strong>만약 몬스터의 공격을 받고 캐릭터의 체력이 0 이하가 되어 죽는다면 -1을 return 해주세요.</strong></p>

<hr>

<h5>제한사항</h5>

<ul>
<li><code>bandage</code>는 [<code>시전 시간</code>, <code>초당 회복량</code>, <code>추가 회복량</code>] 형태의 길이가 3인 정수 배열입니다.

<ul>
<li>1 ≤ <code>시전 시간</code> = <code>t</code> ≤ 50</li>
<li>1 ≤ <code>초당 회복량</code> = <code>x</code> ≤ 100</li>
<li>1 ≤ <code>추가 회복량</code> = <code>y</code> ≤ 100</li>
</ul></li>
<li>1 ≤ <code>health</code> ≤ 1,000</li>
<li>1 ≤ <code>attacks</code>의 길이 ≤ 100

<ul>
<li><code>attacks[i]</code>는 [<code>공격 시간</code>, <code>피해량</code>] 형태의 길이가 2인 정수 배열입니다.</li>
<li><code>attacks</code>는 <code>공격 시간</code>을 기준으로 오름차순 정렬된 상태입니다.</li>
<li><code>attacks</code>의 <code>공격 시간</code>은 모두 다릅니다.</li>
<li>1 ≤ <code>공격 시간</code> ≤ 1,000</li>
<li>1 ≤ <code>피해량</code> ≤ 100</li>
</ul></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>bandage</th>
<th>health</th>
<th>attacks</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[5, 1, 5]</td>
<td>30</td>
<td>[[2, 10], [9, 15], [10, 5], [11, 5]]</td>
<td>5</td>
</tr>
<tr>
<td>[3, 2, 7]</td>
<td>20</td>
<td>[[1, 15], [5, 16], [8, 6]]</td>
<td>-1</td>
</tr>
<tr>
<td>[4, 2, 7]</td>
<td>20</td>
<td>[[1, 15], [5, 16], [8, 6]]</td>
<td>-1</td>
</tr>
<tr>
<td>[1, 1, 1]</td>
<td>5</td>
<td>[[1, 2], [3, 2]]</td>
<td>3</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<p>몬스터의 마지막 공격은 11초에 이루어집니다. 0초부터 11초까지 캐릭터의 상태는 아래 표와 같습니다.</p>
<table class="table">
        <thead><tr>
<th>시간</th>
<th>현재 체력(변화량)</th>
<th>연속 성공</th>
<th>공격</th>
<th>설명</th>
</tr>
</thead>
        <tbody><tr>
<td>0</td>
<td>30</td>
<td>0</td>
<td>X</td>
<td>초기 상태</td>
</tr>
<tr>
<td>1</td>
<td>30(+0)</td>
<td>1</td>
<td>X</td>
<td>최대 체력 이상의 체력을 가질 수 없습니다.</td>
</tr>
<tr>
<td>2</td>
<td>20(-10)</td>
<td>0</td>
<td>O</td>
<td>몬스터의 공격으로 연속 성공이 초기화됩니다.</td>
</tr>
<tr>
<td>3</td>
<td>21(+1)</td>
<td>1</td>
<td>X</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>22(+1)</td>
<td>2</td>
<td>X</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>23(+1)</td>
<td>3</td>
<td>X</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>24(+1)</td>
<td>4</td>
<td>X</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>30(+6)</td>
<td>5 → 0</td>
<td>X</td>
<td>5초 연속 성공해 체력을 5만큼 추가 회복하고 연속 성공이 초기화됩니다.</td>
</tr>
<tr>
<td>8</td>
<td>30(+0)</td>
<td>1</td>
<td>X</td>
<td>최대 체력 이상의 체력을 가질 수 없습니다.</td>
</tr>
<tr>
<td>9</td>
<td>15(-15)</td>
<td>0</td>
<td>O</td>
<td>몬스터의 공격으로 연속 성공이 초기화됩니다.</td>
</tr>
<tr>
<td>10</td>
<td>10(-5)</td>
<td>0</td>
<td>O</td>
<td>몬스터의 공격으로 연속 성공이 초기화됩니다.</td>
</tr>
<tr>
<td>11</td>
<td>5(-5)</td>
<td>0</td>
<td>O</td>
<td>몬스터의 마지막 공격입니다.</td>
</tr>
</tbody>
      </table>
<p>몬스터의 마지막 공격 직후 캐릭터의 체력은 5입니다. 따라서 <code>5</code>을 return 해야 합니다.</p>

<p><strong>입출력 예 #2</strong></p>

<p>몬스터의 마지막 공격은 8초에 이루어집니다. 0초부터 8초까지 캐릭터의 상태는 아래 표와 같습니다.</p>
<table class="table">
        <thead><tr>
<th>시간</th>
<th>현재 체력(변화량)</th>
<th>연속 성공</th>
<th>공격</th>
<th>설명</th>
</tr>
</thead>
        <tbody><tr>
<td>0</td>
<td>20</td>
<td>0</td>
<td>X</td>
<td>초기 상태</td>
</tr>
<tr>
<td>1</td>
<td>5(-15)</td>
<td>0</td>
<td>O</td>
<td>몬스터의 공격으로 연속 성공이 초기화됩니다.</td>
</tr>
<tr>
<td>2</td>
<td>7(+2)</td>
<td>1</td>
<td>X</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>9(+2)</td>
<td>2</td>
<td>X</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>18(+9)</td>
<td>3 → 0</td>
<td>X</td>
<td>3초 연속 성공해 체력을 7만큼 추가 회복하고 연속 성공이 초기화됩니다.</td>
</tr>
<tr>
<td>5</td>
<td>2(-16)</td>
<td>0</td>
<td>O</td>
<td>몬스터의 공격으로 연속 성공이 초기화됩니다.</td>
</tr>
<tr>
<td>6</td>
<td>4(+2)</td>
<td>1</td>
<td>X</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>6(+2)</td>
<td>2</td>
<td>X</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>0(-6)</td>
<td>0</td>
<td>O</td>
<td>몬스터의 마지막 공격을 받아 캐릭터의 체력이 0 이하가 됩니다.</td>
</tr>
</tbody>
      </table>
<p>몬스터의 공격을 받아 캐릭터의 체력이 0 이하가 됩니다. 따라서 <code>-1</code>을 return 해야 합니다.</p>

<p><strong>입출력 예 #3</strong></p>

<p>몬스터의 마지막 공격은 8초에 이루어집니다. 0초부터 5초까지 캐릭터의 상태는 아래 표와 같습니다.</p>
<table class="table">
        <thead><tr>
<th>시간</th>
<th>현재 체력(변화량)</th>
<th>연속 성공</th>
<th>공격</th>
<th>설명</th>
</tr>
</thead>
        <tbody><tr>
<td>0</td>
<td>20</td>
<td>0</td>
<td>X</td>
<td>초기 상태</td>
</tr>
<tr>
<td>1</td>
<td>5(-15)</td>
<td>0</td>
<td>O</td>
<td>몬스터의 공격으로 연속 성공이 초기화됩니다.</td>
</tr>
<tr>
<td>2</td>
<td>7(+2)</td>
<td>1</td>
<td>X</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>9(+2)</td>
<td>2</td>
<td>X</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>11(+2)</td>
<td>3</td>
<td>X</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>-5(-16)</td>
<td>0</td>
<td>O</td>
<td>몬스터의 공격을 받아 캐릭터의 체력이 0 이하가 됩니다.</td>
</tr>
</tbody>
      </table>
<p>몬스터의 공격을 받아 캐릭터의 체력이 0 이하가 됩니다. 따라서 <code>-1</code>을 return 해야 합니다.</p>

<p><strong>입출력 예 #4</strong></p>

<p>몬스터의 마지막 공격은 3초에 이루어집니다. 0초부터 3초까지 캐릭터의 상태는 아래 표와 같습니다.</p>
<table class="table">
        <thead><tr>
<th>시간</th>
<th>현재 체력(변화량)</th>
<th>연속 성공</th>
<th>공격</th>
<th>설명</th>
</tr>
</thead>
        <tbody><tr>
<td>0</td>
<td>5</td>
<td>0</td>
<td>X</td>
<td>초기 상태</td>
</tr>
<tr>
<td>1</td>
<td>3(-2)</td>
<td>0</td>
<td>O</td>
<td>몬스터의 공격으로 연속 성공이 초기화됩니다.</td>
</tr>
<tr>
<td>2</td>
<td>5(+2)</td>
<td>1 → 0</td>
<td>X</td>
<td>1초 연속 성공해 체력을 1만큼 추가 회복하고 연속 성공이 초기화됩니다.</td>
</tr>
<tr>
<td>3</td>
<td>3(-2)</td>
<td>0</td>
<td>O</td>
<td>몬스터의 마지막 공격입니다.</td>
</tr>
</tbody>
      </table>
<p>몬스터의 마지막 공격 직후 캐릭터의 체력은 3입니다. 따라서 <code>3</code>을 return 해야 합니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges