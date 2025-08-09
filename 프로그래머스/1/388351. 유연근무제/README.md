# [level 1] 유연근무제 - 388351 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/388351) 

### 성능 요약

메모리: 9.57 MB, 시간: 1.70 ms

### 구분

코딩테스트 연습 > 2025 프로그래머스 코드챌린지 1차 예선

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2025년 08월 09일 18:20:23

### 문제 설명

<p>프로그래머스 사이트를 운영하는 그렙에서는 재택근무와 함께 출근 희망 시각을 자유롭게 정하는 유연근무제를 시행하고 있습니다. 제도 정착을 위해 오늘부터 일주일 동안 각자 설정한 출근 희망 시각에 늦지 않고 출근한 직원들에게 상품을 주는 이벤트를 진행하려고 합니다. </p>

<p>직원들은 일주일동안 자신이 설정한 <code>출근 희망 시각 + 10분</code>까지 어플로 출근해야 합니다. 예를 들어 출근 희망 시각이 9시 58분인 직원은 10시 8분까지 출근해야 합니다. <strong>단, 토요일, 일요일의 출근 시각은 이벤트에 영향을 끼치지 않습니다.</strong> 직원들은 매일 한 번씩만 어플로 출근하고, 모든 시각은 시에 100을 곱하고 분을 더한 정수로 표현됩니다. 예를 들어 10시 13분은 1013이 되고 9시 58분은 958이 됩니다. </p>

<p>당신은 직원들이 설정한 출근 희망 시각과 실제로 출근한 기록을 바탕으로 상품을 받을 직원이 몇 명인지 알고 싶습니다.</p>

<p>직원 <code>n</code>명이 설정한 출근 희망 시각을 담은 1차원 정수 배열 <code>schedules</code>, 직원들이 일주일 동안 출근한 시각을 담은 2차원 정수 배열 <code>timelogs</code>, 이벤트를 시작한 요일을 의미하는 정수 <code>startday</code>가 매개변수로 주어집니다. 이때 상품을 받을 직원의 수를 return 하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>schedules</code>의 길이 = <code>n</code> ≤ 1,000

<ul>
<li><code>schedules[i]</code>는 <code>i + 1</code>번째 직원이 설정한 출근 희망 시각을 의미합니다.</li>
<li>700 ≤ <code>schedules[i]</code> ≤ 1100</li>
</ul></li>
<li>1 ≤ <code>timelogs</code>의 길이 = <code>n</code> ≤ 1,000

<ul>
<li><code>timelogs[i]</code>의 길이 = 7</li>
<li><code>timelogs[i][j]</code>는 <code>i + 1</code>번째 직원이 이벤트 <code>j + 1</code>일차에 출근한 시각을 의미합니다.</li>
<li>600 ≤ <code>timelogs[i][j]</code> ≤ 2359</li>
</ul></li>
<li>1 ≤ <code>startday</code> ≤ 7

<ul>
<li>1은 월요일, 2는 화요일, 3은 수요일, 4는 목요일, 5는 금요일, 6은 토요일, 7은 일요일에 이벤트를 시작했음을 의미합니다.</li>
</ul></li>
<li>출근 희망 시각과 실제로 출근한 시각을 100으로 나눈 나머지는 59 이하입니다.</li>
</ul>

<hr>

<h5>테스트 케이스 구성 안내</h5>

<p>아래는 테스트 케이스 구성을 나타냅니다. 각 그룹 내의 테스트 케이스를 모두 통과하면 해당 그룹에 할당된 점수를 획득할 수 있습니다.</p>
<table class="table">
        <thead><tr>
<th>그룹</th>
<th>총점</th>
<th>추가 제한 사항</th>
</tr>
</thead>
        <tbody><tr>
<td>#1</td>
<td>10%</td>
<td><code>n</code> = 1. 이벤트 시작일이 월요일이고, 출근 희망 시각이 정각으로 된 입력만 주어집니다.</td>
</tr>
<tr>
<td>#2</td>
<td>10%</td>
<td>이벤트 시작일이 월요일이고, 출근 희망 시각이 정각으로 된 입력만 주어집니다.</td>
</tr>
<tr>
<td>#3</td>
<td>15%</td>
<td>출근 희망 시각이 정각으로 된 입력만 주어집니다.</td>
</tr>
<tr>
<td>#4</td>
<td>15%</td>
<td>이벤트 시작일이 월요일인 입력만 주어집니다.</td>
</tr>
<tr>
<td>#5</td>
<td>50%</td>
<td>제한사항 외 추가조건이 없습니다.</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>schedules</th>
<th>timelogs</th>
<th>startday</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[700, 800, 1100]</td>
<td>[[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809], [1105, 1001, 1002, 600, 1059, 1001, 1100]]</td>
<td>5</td>
<td>3</td>
</tr>
<tr>
<td>[730, 855, 700, 720]</td>
<td>[[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835], [705, 701, 702, 705, 710, 710, 711], [707, 731, 859, 913, 934, 931, 905]]</td>
<td>1</td>
<td>2</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<p>이벤트를 시작한 날은 금요일입니다. 직원 3명의 일주일 간 출근 시각을 나타내면 다음과 같습니다.</p>
<table class="table">
        <thead><tr>
<th>출근 희망 시각</th>
<th>출근 인정 시각</th>
</tr>
</thead>
        <tbody><tr>
<td>7:00</td>
<td>7:10</td>
</tr>
<tr>
<td>8:00</td>
<td>8:10</td>
</tr>
<tr>
<td>11:00</td>
<td>11:10</td>
</tr>
</tbody>
      </table><table class="table">
        <thead><tr>
<th>금</th>
<th>토</th>
<th>일</th>
<th>월</th>
<th>화</th>
<th>수</th>
<th>목</th>
</tr>
</thead>
        <tbody><tr>
<td>7:10</td>
<td>23:59</td>
<td>10:50</td>
<td>7:00</td>
<td>6:50</td>
<td>6:31</td>
<td>6:59</td>
</tr>
<tr>
<td>8:00</td>
<td>8:01</td>
<td>8:05</td>
<td>8:00</td>
<td>7:59</td>
<td>8:10</td>
<td>8:09</td>
</tr>
<tr>
<td>11:05</td>
<td>10:01</td>
<td>10:02</td>
<td>6:00</td>
<td>10:59</td>
<td>10:01</td>
<td>11:00</td>
</tr>
</tbody>
      </table>
<p>모든 직원이 평일에 늦지 않고 출근했습니다. 따라서 상품을 받을 직원은 3명입니다.</p>

<p><strong>입출력 예 #2</strong></p>

<p>이벤트를 시작한 날은 월요일입니다. 직원 4명의 일주일 간 출근 시각을 나타내면 다음과 같습니다. 취소선으로 표시된 시각이 출근이 필요한 평일에 지각한 날입니다. </p>
<table class="table">
        <thead><tr>
<th>출근 희망 시각</th>
<th>출근 인정 시각</th>
</tr>
</thead>
        <tbody><tr>
<td>7:30</td>
<td>7:40</td>
</tr>
<tr>
<td>8:55</td>
<td>9:05</td>
</tr>
<tr>
<td>7:00</td>
<td>7:10</td>
</tr>
<tr>
<td>7:20</td>
<td>7:30</td>
</tr>
</tbody>
      </table><table class="table">
        <thead><tr>
<th>월</th>
<th>화</th>
<th>수</th>
<th>목</th>
<th>금</th>
<th>토</th>
<th>일</th>
</tr>
</thead>
        <tbody><tr>
<td>7:10</td>
<td>7:00</td>
<td>6:50</td>
<td>7:35</td>
<td>7:00</td>
<td>9:31</td>
<td>9:12</td>
</tr>
<tr>
<td><del>9:08</del></td>
<td>9:01</td>
<td>8:05</td>
<td>8:15</td>
<td>8:00</td>
<td>8:31</td>
<td>8:35</td>
</tr>
<tr>
<td>7:05</td>
<td>7:01</td>
<td>7:02</td>
<td>7:05</td>
<td>7:10</td>
<td>7:10</td>
<td>7:11</td>
</tr>
<tr>
<td>7:07</td>
<td><del>7:31</del></td>
<td><del>8:59</del></td>
<td><del>9:13</del></td>
<td><del>9:34</del></td>
<td>9:31</td>
<td>9:05</td>
</tr>
</tbody>
      </table>
<p>첫 번째, 세 번째 직원이 평일에 늦지 않고 출근했습니다. 따라서 상품을 받을 직원은 2명입니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges