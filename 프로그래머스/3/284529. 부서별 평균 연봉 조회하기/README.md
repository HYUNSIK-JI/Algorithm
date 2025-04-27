# [level 3] 부서별 평균 연봉 조회하기 - 284529 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/284529) 

### 성능 요약

메모리: undefined, 시간: 

### 구분

코딩테스트 연습 > GROUP BY

### 채점결과

합계: 100.0 / 100.0

### 제출 일자

2025년 04월 27일 15:24:47

### 문제 설명

<p><code>HR_DEPARTMENT</code> 테이블은 회사의 부서 정보를 담은 테이블입니다. <code>HR_DEPARTMENT</code> 테이블의 구조는 다음과 같으며 <code>DEPT_ID</code>, <code>DEPT_NAME_KR</code>, <code>DEPT_NAME_EN</code>, <code>LOCATION</code>은 각각 부서 ID, 국문 부서명, 영문 부서명, 부서 위치를 의미합니다.</p>
<table class="table">
        <thead><tr>
<th>Column name</th>
<th>Type</th>
<th>Nullable</th>
</tr>
</thead>
        <tbody><tr>
<td>DEPT_ID</td>
<td>VARCHAR</td>
<td>FALSE</td>
</tr>
<tr>
<td>DEPT_NAME_KR</td>
<td>VARCHAR</td>
<td>FALSE</td>
</tr>
<tr>
<td>DEPT_NAME_EN</td>
<td>VARCHAR</td>
<td>FALSE</td>
</tr>
<tr>
<td>LOCATION</td>
<td>VARCHAR</td>
<td>FLASE</td>
</tr>
</tbody>
      </table>
<p><code>HR_EMPLOYEES</code> 테이블은 회사의 사원 정보를 담은 테이블입니다. <code>HR_EMPLOYEES</code> 테이블의 구조는 다음과 같으며 <code>EMP_NO</code>, <code>EMP_NAME</code>, <code>DEPT_ID</code>, <code>POSITION</code>, <code>EMAIL</code>, <code>COMP_TEL</code>, <code>HIRE_DATE</code>, <code>SAL</code>은 각각 사번, 성명, 부서 ID, 직책, 이메일, 전화번호, 입사일, 연봉을 의미합니다.</p>
<table class="table">
        <thead><tr>
<th>Column name</th>
<th>Type</th>
<th>Nullable</th>
</tr>
</thead>
        <tbody><tr>
<td>EMP_NO</td>
<td>VARCHAR</td>
<td>FALSE</td>
</tr>
<tr>
<td>EMP_NAME</td>
<td>VARCHAR</td>
<td>FALSE</td>
</tr>
<tr>
<td>DEPT_ID</td>
<td>VARCHAR</td>
<td>FALSE</td>
</tr>
<tr>
<td>POSITION</td>
<td>VARCHAR</td>
<td>FALSE</td>
</tr>
<tr>
<td>EMAIL</td>
<td>VARCHAR</td>
<td>FALSE</td>
</tr>
<tr>
<td>COMP_TEL</td>
<td>VARCHAR</td>
<td>FALSE</td>
</tr>
<tr>
<td>HIRE_DATE</td>
<td>DATE</td>
<td>FALSE</td>
</tr>
<tr>
<td>SAL</td>
<td>NUMBER</td>
<td>FALSE</td>
</tr>
</tbody>
      </table>
<hr>

<h5>문제</h5>

<p><code>HR_DEPARTMENT</code>와 <code>HR_EMPLOYEES</code> 테이블을 이용해 부서별 평균 연봉을 조회하려 합니다. 부서별로 부서 ID, 영문 부서명, 평균 연봉을 조회하는 SQL문을 작성해주세요.</p>

<p>평균연봉은 소수점 첫째 자리에서 반올림하고 컬럼명은 <code>AVG_SAL</code>로 해주세요.<br>
결과는 부서별 평균 연봉을 기준으로 내림차순 정렬해주세요.</p>

<hr>

<h5>예시</h5>

<p><code>HR_DEPARTMENT</code> 테이블이 다음과 같고</p>
<table class="table">
        <thead><tr>
<th>DEPT_ID</th>
<th>DEPT_NAME_KR</th>
<th>DEPT_NAME_EN</th>
<th>LOCATION</th>
</tr>
</thead>
        <tbody><tr>
<td>D0005</td>
<td>재무팀</td>
<td>Finance</td>
<td>그렙타워 5층</td>
</tr>
<tr>
<td>D0006</td>
<td>구매팀</td>
<td>Purchasing</td>
<td>그렙타워 5층</td>
</tr>
<tr>
<td>D0007</td>
<td>마케팅팀</td>
<td>Marketing</td>
<td>그렙타워 6층</td>
</tr>
</tbody>
      </table>
<p><code>HR_EMPLOYEES</code> 테이블이 다음과 같을 때</p>
<table class="table">
        <thead><tr>
<th>EMP_NO</th>
<th>EMP_NAME</th>
<th>DEPT_ID</th>
<th>POSITION</th>
<th>EMAIL</th>
<th>COMP_TEL</th>
<th>HIRE_DATE</th>
<th>SAL</th>
</tr>
</thead>
        <tbody><tr>
<td>2019003</td>
<td>한동희</td>
<td>D0005</td>
<td>팀장</td>
<td><a href="mailto:donghee_han@grep.com" target="_blank" rel="noopener">donghee_han@grep.com</a></td>
<td>031-8000-1122</td>
<td>2019-03-01</td>
<td>57000000</td>
</tr>
<tr>
<td>2020032</td>
<td>한명지</td>
<td>D0005</td>
<td>팀원</td>
<td><a href="mailto:mungji_han@grep.com" target="_blank" rel="noopener">mungji_han@grep.com</a></td>
<td>031-8000-1123</td>
<td>2020-03-01</td>
<td>52000000</td>
</tr>
<tr>
<td>2022003</td>
<td>김보라</td>
<td>D0005</td>
<td>팀원</td>
<td><a href="mailto:bora_kim@grep.com" target="_blank" rel="noopener">bora_kim@grep.com</a></td>
<td>031-8000-1126</td>
<td>2022-03-01</td>
<td>47000000</td>
</tr>
<tr>
<td>2018005</td>
<td>이재정</td>
<td>D0006</td>
<td>팀장</td>
<td><a href="mailto:jaejung_lee@grep.com" target="_blank" rel="noopener">jaejung_lee@grep.com</a></td>
<td>031-8000-1127</td>
<td>2018-03-01</td>
<td>60000000</td>
</tr>
<tr>
<td>2019032</td>
<td>윤성희</td>
<td>D0006</td>
<td>팀원</td>
<td><a href="mailto:sunghee_yoon@grep.com" target="_blank" rel="noopener">sunghee_yoon@grep.com</a></td>
<td>031-8000-1128</td>
<td>2019-03-01</td>
<td>57000000</td>
</tr>
<tr>
<td>2020009</td>
<td>송영섭</td>
<td>D0006</td>
<td>팀원</td>
<td><a href="mailto:yungseop_song@grep.com" target="_blank" rel="noopener">yungseop_song@grep.com</a></td>
<td>031-8000-1130</td>
<td>2020-03-01</td>
<td>51000000</td>
</tr>
<tr>
<td>2021006</td>
<td>이성주</td>
<td>D0006</td>
<td>팀원</td>
<td><a href="mailto:sungju_lee@grep.com" target="_blank" rel="noopener">sungju_lee@grep.com</a></td>
<td>031-8000-1131</td>
<td>2021-03-01</td>
<td>49000000</td>
</tr>
<tr>
<td>2018004</td>
<td>이주리</td>
<td>D0007</td>
<td>팀장</td>
<td><a href="mailto:joori_lee@grep.com" target="_blank" rel="noopener">joori_lee@grep.com</a></td>
<td>031-8000-1132</td>
<td>2018-03-01</td>
<td>61000000</td>
</tr>
<tr>
<td>2020012</td>
<td>김사랑</td>
<td>D0007</td>
<td>팀원</td>
<td><a href="mailto:sarang_kim@grep.com" target="_blank" rel="noopener">sarang_kim@grep.com</a></td>
<td>031-8000-1133</td>
<td>2020-03-01</td>
<td>54000000</td>
</tr>
<tr>
<td>2021018</td>
<td>김히라</td>
<td>D0007</td>
<td>팀원</td>
<td><a href="mailto:heera_kim@grep.com" target="_blank" rel="noopener">heera_kim@grep.com</a></td>
<td>031-8000-1136</td>
<td>2021-03-01</td>
<td>49000000</td>
</tr>
</tbody>
      </table>
<p>SQL을 실행하면 다음과 같이 출력되어야 합니다.</p>
<table class="table">
        <thead><tr>
<th>DEPT_ID</th>
<th>DEPT_NAME_EN</th>
<th>AVG_SAL</th>
</tr>
</thead>
        <tbody><tr>
<td>D0007</td>
<td>Marketing</td>
<td>54666667</td>
</tr>
<tr>
<td>D0006</td>
<td>Purchasing</td>
<td>54250000</td>
</tr>
<tr>
<td>D0005</td>
<td>Finance</td>
<td>52000000</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges