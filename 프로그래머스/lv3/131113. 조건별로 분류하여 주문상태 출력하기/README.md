# [level 3] 조건별로 분류하여 주문상태 출력하기 - 131113 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/131113) 

### 성능 요약

메모리: 0.0 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > String， Date

### 채점결과

Empty

### 문제 설명

<p>다음은 식품공장의 주문정보를 담은 <code>FOOD_ORDER</code> 테이블입니다. <code>FOOD_ORDER</code> 테이블은 다음과 같으며 <code>ORDER_ID</code>, <code>PRODUCT_ID</code>, <code>AMOUNT</code>, <code>PRODUCE_DATE</code>, <code>IN_DATE</code>,<code>OUT_DATE</code>,<code>FACTORY_ID</code>, <code>WAREHOUSE_ID</code>는 각각 주문 ID, 제품 ID, 주문양, 생산일자, 입고일자, 출고일자, 공장 ID, 창고 ID를 의미합니다.</p>
<table class="table">
        <thead><tr>
<th>Column name</th>
<th>Type</th>
<th>Nullable</th>
</tr>
</thead>
        <tbody><tr>
<td>ORDER_ID</td>
<td>VARCHAR(10)</td>
<td>FALSE</td>
</tr>
<tr>
<td>PRODUCT_ID</td>
<td>VARCHAR(5)</td>
<td>FALSE</td>
</tr>
<tr>
<td>AMOUNT</td>
<td>NUMBER</td>
<td>FALSE</td>
</tr>
<tr>
<td>PRODUCE_DATE</td>
<td>DATE</td>
<td>TRUE</td>
</tr>
<tr>
<td>IN_DATE</td>
<td>DATE</td>
<td>TRUE</td>
</tr>
<tr>
<td>OUT_DATE</td>
<td>DATE</td>
<td>TRUE</td>
</tr>
<tr>
<td>FACTORY_ID</td>
<td>VARCHAR(10)</td>
<td>FALSE</td>
</tr>
<tr>
<td>WAREHOUSE_ID</td>
<td>VARCHAR(10)</td>
<td>FALSE</td>
</tr>
</tbody>
      </table>
<hr>

<h5>문제</h5>

<p><code>FOOD_ORDER</code> 테이블에서 5월 1일을 기준으로 주문 ID, 제품 ID, 출고일자, 출고여부를 조회하는 SQL문을 작성해주세요. 출고여부는 5월 1일까지 출고완료로 이 후 날짜는 출고 대기로 미정이면 출고미정으로 출력해주시고, 결과는 주문 ID를 기준으로 오름차순 정렬해주세요.</p>

<hr>

<h5>예시</h5>

<p><code>FOOD_ORDER</code> 테이블이 다음과 같을 때</p>
<table class="table">
        <thead><tr>
<th>ORDER_ID</th>
<th>PRODUCT_ID</th>
<th>AMOUNT</th>
<th>PRODUCE_DATE</th>
<th>IN_DATE</th>
<th>OUT_DATE</th>
<th>FACTORY_ID</th>
<th>WAREHOUSE_ID</th>
</tr>
</thead>
        <tbody><tr>
<td>OD00000051</td>
<td>P0002</td>
<td>4000</td>
<td>2022-04-01</td>
<td>2022-04-21</td>
<td>2022-04-21</td>
<td>FT19970003</td>
<td>WH0005</td>
</tr>
<tr>
<td>OD00000052</td>
<td>P0003</td>
<td>2500</td>
<td>2022-04-10</td>
<td>2022-04-27</td>
<td>2022-04-27</td>
<td>FT19970003</td>
<td>WH0006</td>
</tr>
<tr>
<td>OD00000053</td>
<td>P0005</td>
<td>6200</td>
<td>2022-04-15</td>
<td>2022-04-30</td>
<td>2022-05-01</td>
<td>FT19940003</td>
<td>WH0003</td>
</tr>
<tr>
<td>OD00000054</td>
<td>P0006</td>
<td>1000</td>
<td>2022-04-21</td>
<td>2022-04-30</td>
<td>NULL</td>
<td>FT19940003</td>
<td>WH0009</td>
</tr>
<tr>
<td>OD00000055</td>
<td>P0008</td>
<td>1500</td>
<td>2022-04-25</td>
<td>2022-05-11</td>
<td>2022-05-11</td>
<td>FT19980003</td>
<td>WH0009</td>
</tr>
</tbody>
      </table>
<p>SQL을 실행하면 다음과 같이 출력되어야 합니다.</p>
<table class="table">
        <thead><tr>
<th>ORDER_ID</th>
<th>PRODUCT_ID</th>
<th>OUT_DATE</th>
<th>출고여부</th>
</tr>
</thead>
        <tbody><tr>
<td>OD00000051</td>
<td>P0002</td>
<td>2022-04-21</td>
<td>출고완료</td>
</tr>
<tr>
<td>OD00000052</td>
<td>P0003</td>
<td>2022-04-27</td>
<td>출고완료</td>
</tr>
<tr>
<td>OD00000053</td>
<td>P0005</td>
<td>2022-05-01</td>
<td>출고완료</td>
</tr>
<tr>
<td>OD00000054</td>
<td>P0006</td>
<td></td>
<td>출고미정</td>
</tr>
<tr>
<td>OD00000055</td>
<td>P0008</td>
<td>2022-05-11</td>
<td>출고대기</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges