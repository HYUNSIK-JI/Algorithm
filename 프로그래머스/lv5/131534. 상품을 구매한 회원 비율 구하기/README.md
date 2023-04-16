# [level 5] 상품을 구매한 회원 비율 구하기 - 131534 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/131534) 

### 성능 요약

메모리: 0.0 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > JOIN

### 채점결과

Empty

### 문제 설명

<p>다음은 어느 의류 쇼핑몰에 가입한 회원 정보를 담은 <code>USER_INFO</code> 테이블과 온라인 상품 판매 정보를 담은 <code>ONLINE_SALE</code> 테이블 입니다. <code>USER_INFO</code> 테이블은 아래와 같은 구조로 되어있으며 <code>USER_ID</code>, <code>GENDER</code>, <code>AGE</code>, <code>JOINED</code>는 각각 회원 ID, 성별, 나이, 가입일을 나타냅니다.</p>
<table class="table">
        <thead><tr>
<th>Column name</th>
<th>Type</th>
<th>Nullable</th>
</tr>
</thead>
        <tbody><tr>
<td>USER_ID</td>
<td>INTEGER</td>
<td>FALSE</td>
</tr>
<tr>
<td>GENDER</td>
<td>TINYINT(1)</td>
<td>TRUE</td>
</tr>
<tr>
<td>AGE</td>
<td>INTEGER</td>
<td>TRUE</td>
</tr>
<tr>
<td>JOINED</td>
<td>DATE</td>
<td>FALSE</td>
</tr>
</tbody>
      </table>
<p><code>GENDER</code> 컬럼은 비어있거나 0 또는 1의 값을 가지며 0인 경우 남자를, 1인 경우는 여자를 나타냅니다.</p>

<p><code>ONLINE_SALE</code> 테이블은 아래와 같은 구조로 되어있으며 <code>ONLINE_SALE_ID</code>, <code>USER_ID</code>, <code>PRODUCT_ID</code>, <code>SALES_AMOUNT</code>, <code>SALES_DATE</code>는 각각 온라인 상품 판매 ID, 회원 ID, 상품 ID, 판매량, 판매일을 나타냅니다.</p>
<table class="table">
        <thead><tr>
<th>Column name</th>
<th>Type</th>
<th>Nullable</th>
</tr>
</thead>
        <tbody><tr>
<td>ONLINE_SALE_ID</td>
<td>INTEGER</td>
<td>FALSE</td>
</tr>
<tr>
<td>USER_ID</td>
<td>INTEGER</td>
<td>FALSE</td>
</tr>
<tr>
<td>PRODUCT_ID</td>
<td>INTEGER</td>
<td>FALSE</td>
</tr>
<tr>
<td>SALES_AMOUNT</td>
<td>INTEGER</td>
<td>FALSE</td>
</tr>
<tr>
<td>SALES_DATE</td>
<td>DATE</td>
<td>FALSE</td>
</tr>
</tbody>
      </table>
<p>동일한 날짜, 회원 ID, 상품 ID 조합에 대해서는 하나의 판매 데이터만 존재합니다.</p>

<hr>

<h5>문제</h5>

<p><code>USER_INFO</code> 테이블과 <code>ONLINE_SALE</code> 테이블에서 2021년에 가입한 전체 회원들 중 상품을 구매한 회원수와 상품을 구매한 회원의 비율(=2021년에 가입한 회원 중 상품을 구매한 회원수 / 2021년에 가입한 전체 회원 수)을 년, 월 별로 출력하는 SQL문을 작성해주세요. 상품을 구매한 회원의 비율은 소수점 두번째자리에서 반올림하고, 전체 결과는 년을 기준으로 오름차순 정렬해주시고 년이 같다면 월을 기준으로 오름차순 정렬해주세요.</p>

<hr>

<h5>예시</h5>

<p>예를 들어 <code>USER_INFO</code> 테이블이 다음과 같고 </p>
<table class="table">
        <thead><tr>
<th>USER_ID</th>
<th>GENDER</th>
<th>AGE</th>
<th>JOINED</th>
</tr>
</thead>
        <tbody><tr>
<td>1</td>
<td>1</td>
<td>26</td>
<td>2021-06-01</td>
</tr>
<tr>
<td>2</td>
<td>NULL</td>
<td>NULL</td>
<td>2021-06-25</td>
</tr>
<tr>
<td>3</td>
<td>0</td>
<td>NULL</td>
<td>2021-06-30</td>
</tr>
<tr>
<td>4</td>
<td>0</td>
<td>31</td>
<td>2021-07-03</td>
</tr>
<tr>
<td>5</td>
<td>1</td>
<td>25</td>
<td>2022-01-09</td>
</tr>
<tr>
<td>6</td>
<td>1</td>
<td>33</td>
<td>2022-02-14</td>
</tr>
</tbody>
      </table>
<p><code>ONLINE_SALE</code> 이 다음과 같다면</p>
<table class="table">
        <thead><tr>
<th>ONLINE_SALE_ID</th>
<th>USER_ID</th>
<th>PRODUCT_ID</th>
<th>SALES_AMOUNT</th>
<th>SALES_DATE</th>
</tr>
</thead>
        <tbody><tr>
<td>1</td>
<td>1</td>
<td>54</td>
<td>1</td>
<td>2022-01-01</td>
</tr>
<tr>
<td>2</td>
<td>1</td>
<td>3</td>
<td>2</td>
<td>2022-01-25</td>
</tr>
<tr>
<td>3</td>
<td>4</td>
<td>34</td>
<td>1</td>
<td>2022-01-30</td>
</tr>
<tr>
<td>4</td>
<td>6</td>
<td>253</td>
<td>3</td>
<td>2022-02-03</td>
</tr>
<tr>
<td>5</td>
<td>2</td>
<td>31</td>
<td>2</td>
<td>2022-02-09</td>
</tr>
<tr>
<td>6</td>
<td>5</td>
<td>35</td>
<td>1</td>
<td>2022-02-14</td>
</tr>
<tr>
<td>7</td>
<td>5</td>
<td>57</td>
<td>1</td>
<td>2022-02-18</td>
</tr>
</tbody>
      </table>
<p>2021년에 가입한 회원은 <code>USER_ID</code>가 1, 2, 3, 4 인 회원들로 총 4명 입니다. <code>ONLINE_SALE</code> 테이블에서 해당 회원들에 대한 판매 데이터는 다음과 같습니다.</p>
<table class="table">
        <thead><tr>
<th>ONLINE_SALE_ID</th>
<th>USER_ID</th>
<th>PRODUCT_ID</th>
<th>SALES_AMOUNT</th>
<th>SALES_DATE</th>
</tr>
</thead>
        <tbody><tr>
<td>1</td>
<td>1</td>
<td>54</td>
<td>1</td>
<td>2022-01-01</td>
</tr>
<tr>
<td>2</td>
<td>1</td>
<td>3</td>
<td>2</td>
<td>2022-01-25</td>
</tr>
<tr>
<td>3</td>
<td>4</td>
<td>34</td>
<td>1</td>
<td>2022-01-30</td>
</tr>
<tr>
<td>5</td>
<td>2</td>
<td>31</td>
<td>2</td>
<td>2022-02-09</td>
</tr>
</tbody>
      </table>
<p>그러므로 년, 월 별로 상품을 구매한 회원수와 상품을 구매한 회원의 비율을 구하고 결과를 정렬하면 다음과 같아야 합니다.</p>
<table class="table">
        <thead><tr>
<th>YEAR</th>
<th>MONTH</th>
<th>PUCHASED_USERS</th>
<th>PUCHASED_RATIO</th>
</tr>
</thead>
        <tbody><tr>
<td>2022</td>
<td>1</td>
<td>2</td>
<td>0.5</td>
</tr>
<tr>
<td>2022</td>
<td>2</td>
<td>1</td>
<td>0.3</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges