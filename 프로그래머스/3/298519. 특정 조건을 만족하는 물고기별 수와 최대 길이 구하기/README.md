# [level 3] 특정 조건을 만족하는 물고기별 수와 최대 길이 구하기 - 298519 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/298519) 

### 성능 요약

메모리: undefined, 시간: 

### 구분

코딩테스트 연습 > GROUP BY

### 채점결과

합계: 100.0 / 100.0

### 제출 일자

2024년 07월 28일 13:38:54

### 문제 설명

<p>낚시앱에서 사용하는 <code>FISH_INFO</code> 테이블은 잡은 물고기들의 정보를 담고 있습니다. <code>FISH_INFO</code> 테이블의 구조는 다음과 같으며 <code>ID</code>, <code>FISH_TYPE</code>, <code>LENGTH</code>, <code>TIME</code>은 각각 잡은 물고기의 ID, 물고기의 종류(숫자), 잡은 물고기의 길이(cm), 물고기를 잡은 날짜를 나타냅니다. </p>
<table class="table">
        <thead><tr>
<th>Column name</th>
<th>Type</th>
<th>Nullable</th>
</tr>
</thead>
        <tbody><tr>
<td>ID</td>
<td>INTEGER</td>
<td>FALSE</td>
</tr>
<tr>
<td>FISH_TYPE</td>
<td>INTEGER</td>
<td>FALSE</td>
</tr>
<tr>
<td>LENGTH</td>
<td>FLOAT</td>
<td>TRUE</td>
</tr>
<tr>
<td>TIME</td>
<td>DATE</td>
<td>FALSE</td>
</tr>
</tbody>
      </table>
<p>단, 잡은 물고기의 길이가 10cm 이하일 경우에는 <code>LENGTH</code> 가 NULL 이며, <code>LENGTH</code> 에 NULL 만 있는 경우는 없습니다.</p>

<hr>

<h5>문제</h5>

<p><code>FISH_INFO</code>에서 평균 길이가 33cm 이상인 물고기들을 종류별로 분류하여 잡은 수, 최대 길이, 물고기의 종류를 출력하는 SQL문을 작성해주세요. 결과는 물고기 종류에 대해 오름차순으로 정렬해주시고, 10cm이하의 물고기들은 10cm로 취급하여 평균 길이를 구해주세요.</p>

<p>컬럼명은 물고기의 종류 'FISH_TYPE', 잡은 수 'FISH_COUNT', 최대 길이 'MAX_LENGTH'로 해주세요.</p>

<hr>

<h5>예시</h5>

<p>예를 들어 <code>FISH_INFO</code> 테이블이 다음과 같다면</p>
<table class="table">
        <thead><tr>
<th>ID</th>
<th>FISH_TYPE</th>
<th>LENGTH</th>
<th>TIME</th>
</tr>
</thead>
        <tbody><tr>
<td>0</td>
<td>0</td>
<td>30</td>
<td>2021/12/04</td>
</tr>
<tr>
<td>1</td>
<td>0</td>
<td>50</td>
<td>2020/03/07</td>
</tr>
<tr>
<td>2</td>
<td>0</td>
<td>40</td>
<td>2020/03/07</td>
</tr>
<tr>
<td>3</td>
<td>1</td>
<td>30</td>
<td>2022/03/09</td>
</tr>
<tr>
<td>4</td>
<td>1</td>
<td>NULL</td>
<td>2022/04/08</td>
</tr>
<tr>
<td>5</td>
<td>2</td>
<td>32</td>
<td>2020/04/28</td>
</tr>
</tbody>
      </table>
<p>물고기 종류가 0인 물고기들의 평균 길이는 (30 + 50 + 40) / 3 = 40cm 이고 물고기 종류가 1인 물고기들의 평균 길이는 (30 + 10) / 2 = 20cm 이며, 물고기 종류(가 2인 물고기들의 평균 길이는 (32) / 1 = 32cm 입니다. 따라서 평균길이가 33cm 인 물고기 종류는 0 이므로, 총 잡은 수는 3마리, 최대 길이는 50cm 이므로 결과는 다음과 같아야 합니다. </p>
<table class="table">
        <thead><tr>
<th>FISH_COUNT</th>
<th>MAX_LENGTH</th>
<th>FISH_TYPE</th>
</tr>
</thead>
        <tbody><tr>
<td>3</td>
<td>50</td>
<td>0</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges