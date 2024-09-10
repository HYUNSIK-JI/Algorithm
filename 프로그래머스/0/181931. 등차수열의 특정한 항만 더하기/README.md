# [level 0] 등차수열의 특정한 항만 더하기 - 181931 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181931) 

### 성능 요약

메모리: 10 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 09월 10일 16:16:07

### 문제 설명

<p>두 정수 <code>a</code>, <code>d</code>와 길이가 n인 boolean 배열 <code>included</code>가 주어집니다. 첫째항이 <code>a</code>, 공차가 <code>d</code>인 등차수열에서 <code>included[i]</code>가 i + 1항을 의미할 때, 이 등차수열의 1항부터 n항까지 <code>included</code>가 true인 항들만 더한 값을 return 하는 solution 함수를 작성해 주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>a</code> ≤ 100</li>
<li>1 ≤ <code>d</code> ≤ 100</li>
<li>1 ≤ <code>included</code>의 길이 ≤ 100</li>
<li><code>included</code>에는 true가 적어도 하나 존재합니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>a</th>
<th>d</th>
<th>included</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>3</td>
<td>4</td>
<td>[true, false, false, true, true]</td>
<td>37</td>
</tr>
<tr>
<td>7</td>
<td>1</td>
<td>[false, false, false, true, false, false, false]</td>
<td>10</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>예제 1번은 <code>a</code>와 <code>d</code>가 각각 3, 4이고 <code>included</code>의 길이가 5입니다. 이를 표로 나타내면 다음과 같습니다.</li>
</ul>

<p>||1항|2항|3항|4항|5항|</p>

<p>|-|-|---|---|---|---|</p>

<p>|등차수열|3|7|11|15|19|</p>

<p>|included|true|false|false|true|true|</p>
<div class="highlight"><pre class="codehilite"><code>따라서 true에 해당하는 1항, 4항, 5항을 더한 3 + 15 + 19 = 37을 return 합니다.
</code></pre></div>
<p>입출력 예 #2</p>

<ul>
<li>예제 2번은 <code>a</code>와 <code>d</code>가 각각 7, 1이고 <code>included</code>의 길이가 7입니다. 이를 표로 나타내면 다음과 같습니다.</li>
</ul>

<p>||1항|2항|3항|4항|5항|6항|7항|</p>

<p>|-|-|---|---|---|---|---|---|</p>

<p>|등차수열|7|8|9|10|11|12|13|</p>

<p>|included|false|false|false|true|false|false|false|</p>
<div class="highlight"><pre class="codehilite"><code>따라서 4항만 true이므로 10을 return 합니다.
</code></pre></div>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges