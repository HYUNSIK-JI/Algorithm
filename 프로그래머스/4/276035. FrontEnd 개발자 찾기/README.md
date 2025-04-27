# [level 4] FrontEnd 개발자 찾기 - 276035 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/276035) 

### 성능 요약

메모리: undefined, 시간: 

### 구분

코딩테스트 연습 > JOIN

### 채점결과

합계: 100.0 / 100.0

### 제출 일자

2025년 04월 27일 15:38:24

### 문제 설명

<p><code>SKILLCODES</code> 테이블은 개발자들이 사용하는 프로그래밍 언어에 대한 정보를 담은 테이블입니다. <code>SKILLCODES</code> 테이블의 구조는 다음과 같으며,  <code>NAME</code>, <code>CATEGORY</code>, <code>CODE</code>는 각각 스킬의 이름, 스킬의 범주, 스킬의 코드를 의미합니다. 스킬의 코드는 2진수로 표현했을 때 각 bit로 구분될 수 있도록 2의 제곱수로 구성되어 있습니다.</p>
<table class="table">
        <thead><tr>
<th>NAME</th>
<th>TYPE</th>
<th>UNIQUE</th>
<th>NULLABLE</th>
</tr>
</thead>
        <tbody><tr>
<td>NAME</td>
<td>VARCHAR(N)</td>
<td>Y</td>
<td>N</td>
</tr>
<tr>
<td>CATEGORY</td>
<td>VARCHAR(N)</td>
<td>N</td>
<td>N</td>
</tr>
<tr>
<td>CODE</td>
<td>INTEGER</td>
<td>Y</td>
<td>N</td>
</tr>
</tbody>
      </table>
<p><code>DEVELOPERS</code> 테이블은 개발자들의 프로그래밍 스킬 정보를 담은 테이블입니다. <code>DEVELOPERS</code> 테이블의 구조는 다음과 같으며, <code>ID</code>, <code>FIRST_NAME</code>, <code>LAST_NAME</code>, <code>EMAIL</code>, <code>SKILL_CODE</code>는 각각 개발자의 ID, 이름, 성, 이메일, 스킬 코드를 의미합니다. <code>SKILL_CODE</code> 컬럼은 INTEGER 타입이고, 2진수로 표현했을 때 각 bit는 <code>SKILLCODES</code> 테이블의 코드를 의미합니다.</p>
<table class="table">
        <thead><tr>
<th>NAME</th>
<th>TYPE</th>
<th>UNIQUE</th>
<th>NULLABLE</th>
</tr>
</thead>
        <tbody><tr>
<td>ID</td>
<td>VARCHAR(N)</td>
<td>Y</td>
<td>N</td>
</tr>
<tr>
<td>FIRST_NAME</td>
<td>VARCHAR(N)</td>
<td>N</td>
<td>Y</td>
</tr>
<tr>
<td>LAST_NAME</td>
<td>VARCHAR(N)</td>
<td>N</td>
<td>Y</td>
</tr>
<tr>
<td>EMAIL</td>
<td>VARCHAR(N)</td>
<td>Y</td>
<td>N</td>
</tr>
<tr>
<td>SKILL_CODE</td>
<td>INTEGER</td>
<td>N</td>
<td>N</td>
</tr>
</tbody>
      </table>
<p>예를 들어 어떤 개발자의 <code>SKILL_CODE</code>가 400 (=b'110010000')이라면, 이는 <code>SKILLCODES</code> 테이블에서 CODE가 256 (=b'100000000'), 128 (=b'10000000'), 16 (=b'10000') 에 해당하는 스킬을 가졌다는 것을 의미합니다.</p>

<hr>

<h5>문제</h5>

<p><code>DEVELOPERS</code> 테이블에서 Front End 스킬을 가진 개발자의 정보를 조회하려 합니다. 조건에 맞는 개발자의 ID, 이메일, 이름, 성을 조회하는 SQL 문을 작성해 주세요.</p>

<p>결과는 ID를 기준으로 오름차순 정렬해 주세요.</p>

<hr>

<h5>예시</h5>

<p>예를 들어 <code>SKILLCODES</code> 테이블이 다음과 같고,</p>
<table class="table">
        <thead><tr>
<th>NAME</th>
<th>CATEGORY</th>
<th>CODE</th>
</tr>
</thead>
        <tbody><tr>
<td>C++</td>
<td>Back End</td>
<td>4</td>
</tr>
<tr>
<td>JavaScript</td>
<td>Front End</td>
<td>16</td>
</tr>
<tr>
<td>Java</td>
<td>Back End</td>
<td>128</td>
</tr>
<tr>
<td>Python</td>
<td>Back End</td>
<td>256</td>
</tr>
<tr>
<td>C#</td>
<td>Back End</td>
<td>1024</td>
</tr>
<tr>
<td>React</td>
<td>Front End</td>
<td>2048</td>
</tr>
<tr>
<td>Vue</td>
<td>Front End</td>
<td>8192</td>
</tr>
<tr>
<td>Node.js</td>
<td>Back End</td>
<td>16384</td>
</tr>
</tbody>
      </table>
<p><code>DEVELOPERS</code> 테이블이 다음과 같다면</p>
<table class="table">
        <thead><tr>
<th>ID</th>
<th>FIRST_NAME</th>
<th>LAST_NAME</th>
<th>EMAIL</th>
<th>SKILL_CODE</th>
</tr>
</thead>
        <tbody><tr>
<td>D165</td>
<td>Jerami</td>
<td>Edwards</td>
<td><code>jerami_edwards@grepp.co</code></td>
<td>400</td>
</tr>
<tr>
<td>D161</td>
<td>Carsen</td>
<td>Garza</td>
<td><code>carsen_garza@grepp.co</code></td>
<td>2048</td>
</tr>
<tr>
<td>D164</td>
<td>Kelly</td>
<td>Grant</td>
<td><code>kelly_grant@grepp.co</code></td>
<td>1024</td>
</tr>
<tr>
<td>D163</td>
<td>Luka</td>
<td>Cory</td>
<td><code>luka_cory@grepp.co</code></td>
<td>16384</td>
</tr>
<tr>
<td>D162</td>
<td>Cade</td>
<td>Cunningham</td>
<td><code>cade_cunningham@grepp.co</code></td>
<td>8452</td>
</tr>
</tbody>
      </table>
<p>다음과 같이 <code>DEVELOPERS</code> 테이블에 포함된 개발자 중 Front End 스킬을 가진을 가진 개발자의 정보가 결과에 나와야 합니다.</p>
<table class="table">
        <thead><tr>
<th>ID</th>
<th>EMAIL</th>
<th>FIRST_NAME</th>
<th>LAST_NAME</th>
</tr>
</thead>
        <tbody><tr>
<td>D161</td>
<td><code>carsen_garza@grepp.co</code></td>
<td>Carsen</td>
<td>Garza</td>
</tr>
<tr>
<td>D162</td>
<td><code>cade_cunningham@grepp.co</code></td>
<td>Cade</td>
<td>Cunningham</td>
</tr>
<tr>
<td>D165</td>
<td><code>jerami_edwards@grepp.co</code></td>
<td>Jerami</td>
<td>Edwards</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges