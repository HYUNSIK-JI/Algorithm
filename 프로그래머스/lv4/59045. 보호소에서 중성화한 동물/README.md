# [level 4] 보호소에서 중성화한 동물 - 59045 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/59045) 

### 성능 요약

메모리: 0.0 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > JOIN

### 채점결과

Empty

### 문제 설명

<p><code>ANIMAL_INS</code> 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. <code>ANIMAL_INS</code> 테이블 구조는 다음과 같으며, <code>ANIMAL_ID</code>, <code>ANIMAL_TYPE</code>, <code>DATETIME</code>, <code>INTAKE_CONDITION</code>, <code>NAME</code>, <code>SEX_UPON_INTAKE</code>는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.</p>
<table class="table">
        <thead><tr>
<th>NAME</th>
<th>TYPE</th>
<th>NULLABLE</th>
</tr>
</thead>
        <tbody><tr>
<td>ANIMAL_ID</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
<tr>
<td>ANIMAL_TYPE</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
<tr>
<td>DATETIME</td>
<td>DATETIME</td>
<td>FALSE</td>
</tr>
<tr>
<td>INTAKE_CONDITION</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
<tr>
<td>NAME</td>
<td>VARCHAR(N)</td>
<td>TRUE</td>
</tr>
<tr>
<td>SEX_UPON_INTAKE</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
</tbody>
      </table>
<p><code>ANIMAL_OUTS</code> 테이블은 동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블입니다. <code>ANIMAL_OUTS</code> 테이블 구조는 다음과 같으며, <code>ANIMAL_ID</code>, <code>ANIMAL_TYPE</code>, <code>DATETIME</code>, <code>NAME</code>, <code>SEX_UPON_OUTCOME</code>는 각각 동물의 아이디, 생물 종, 입양일, 이름, 성별 및 중성화 여부를 나타냅니다. <code>ANIMAL_OUTS</code> 테이블의 <code>ANIMAL_ID</code>는 <code>ANIMAL_INS</code>의 <code>ANIMAL_ID</code>의 외래 키입니다.</p>
<table class="table">
        <thead><tr>
<th>NAME</th>
<th>TYPE</th>
<th>NULLABLE</th>
</tr>
</thead>
        <tbody><tr>
<td>ANIMAL_ID</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
<tr>
<td>ANIMAL_TYPE</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
<tr>
<td>DATETIME</td>
<td>DATETIME</td>
<td>FALSE</td>
</tr>
<tr>
<td>NAME</td>
<td>VARCHAR(N)</td>
<td>TRUE</td>
</tr>
<tr>
<td>SEX_UPON_OUTCOME</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
</tbody>
      </table>
<p>보호소에서 중성화 수술을 거친 동물 정보를 알아보려 합니다. 보호소에 들어올 당시에는 중성화<sup id="fnref1"><a href="#fn1">1</a></sup>되지 않았지만, 보호소를 나갈 당시에는 중성화된 동물의 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회하는 SQL 문을 작성해주세요.</p>

<h5>예시</h5>

<p>예를 들어, <code>ANIMAL_INS</code> 테이블과 <code>ANIMAL_OUTS</code> 테이블이 다음과 같다면</p>

<p><code>ANIMAL_INS</code></p>
<table class="table">
        <thead><tr>
<th>ANIMAL_ID</th>
<th>ANIMAL_TYPE</th>
<th>DATETIME</th>
<th>INTAKE_CONDITION</th>
<th>NAME</th>
<th>SEX_UPON_INTAKE</th>
</tr>
</thead>
        <tbody><tr>
<td>A367438</td>
<td>Dog</td>
<td>2015-09-10 16:01:00</td>
<td>Normal</td>
<td>Cookie</td>
<td>Spayed Female</td>
</tr>
<tr>
<td>A382192</td>
<td>Dog</td>
<td>2015-03-13 13:14:00</td>
<td>Normal</td>
<td>Maxwell 2</td>
<td>Intact Male</td>
</tr>
<tr>
<td>A405494</td>
<td>Dog</td>
<td>2014-05-16 14:17:00</td>
<td>Normal</td>
<td>Kaila</td>
<td>Spayed Female</td>
</tr>
<tr>
<td>A410330</td>
<td>Dog</td>
<td>2016-09-11 14:09:00</td>
<td>Sick</td>
<td>Chewy</td>
<td>Intact Female</td>
</tr>
</tbody>
      </table>
<p><code>ANIMAL_OUTS</code></p>
<table class="table">
        <thead><tr>
<th>ANIMAL_ID</th>
<th>ANIMAL_TYPE</th>
<th>DATETIME</th>
<th>NAME</th>
<th>SEX_UPON_OUTCOME</th>
</tr>
</thead>
        <tbody><tr>
<td>A367438</td>
<td>Dog</td>
<td>2015-09-12 13:30:00</td>
<td>Cookie</td>
<td>Spayed Female</td>
</tr>
<tr>
<td>A382192</td>
<td>Dog</td>
<td>2015-03-16 13:46:00</td>
<td>Maxwell 2</td>
<td>Neutered Male</td>
</tr>
<tr>
<td>A405494</td>
<td>Dog</td>
<td>2014-05-20 11:44:00</td>
<td>Kaila</td>
<td>Spayed Female</td>
</tr>
<tr>
<td>A410330</td>
<td>Dog</td>
<td>2016-09-13 13:46:00</td>
<td>Chewy</td>
<td>Spayed Female</td>
</tr>
</tbody>
      </table>
<ul>
<li>Cookie는 보호소에 들어올 당시에 이미 중성화되어있었습니다.</li>
<li>Maxwell 2는 보호소에 들어온 후 중성화되었습니다.</li>
<li>Kaila는 보호소에 들어올 당시에 이미 중성화되어있었습니다.</li>
<li>Chewy는 보호소에 들어온 후 중성화되었습니다.</li>
</ul>

<p>따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.</p>
<table class="table">
        <thead><tr>
<th>ANIMAL_ID</th>
<th>ANIMAL_TYPE</th>
<th>NAME</th>
</tr>
</thead>
        <tbody><tr>
<td>A382192</td>
<td>Dog</td>
<td>Maxwell 2</td>
</tr>
<tr>
<td>A410330</td>
<td>Dog</td>
<td>Chewy</td>
</tr>
</tbody>
      </table>
<hr>

<p>본 문제는 <a href="https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-intakes-and-outcomes" target="_blank" rel="noopener">Kaggle의 "Austin Animal Center Shelter Intakes and Outcomes"</a>에서 제공하는 데이터를 사용하였으며 <a href="https://opendatacommons.org/licenses/odbl/1.0/" target="_blank" rel="noopener">ODbL</a>의 적용을 받습니다.</p>

<div class="footnotes">
<hr>
<ol>

<li id="fn1">
<p>중성화를 거치지 않은 동물은 <code>성별 및 중성화 여부</code>에 Intact, 중성화를 거친 동물은 <code>Spayed</code> 또는 <code>Neutered</code>라고 표시되어있습니다.&nbsp;<a href="#fnref1">↩</a></p>
</li>

</ol>
</div>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges