# [unrated] 부대복귀 - 132266 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/132266) 

### 성능 요약

메모리: 51 MB, 시간: 138.69 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>강철부대의 각 부대원이 여러 지역에 뿔뿔이 흩어져 특수 임무를 수행 중입니다. 지도에서 강철부대가 위치한 지역을 포함한 각 지역은 유일한 번호로 구분되며, 두 지역 간의 길을 통과하는 데 걸리는 시간은 모두 1로 동일합니다. 임무를 수행한 각 부대원은 지도 정보를 이용하여 최단시간에 부대로 복귀하고자 합니다. 다만 적군의 방해로 인해, 임무의 시작 때와 다르게 되돌아오는 경로가 없어져 복귀가 불가능한 부대원도 있을 수 있습니다.</p>

<p>강철부대가 위치한 지역을 포함한 총지역의 수 <code>n</code>, 두 지역을 왕복할 수 있는 길 정보를 담은 2차원 정수 배열 <code>roads</code>, 각 부대원이 위치한 서로 다른 지역들을 나타내는 정수 배열 <code>sources</code>, 강철부대의 지역 <code>destination</code>이 주어졌을 때, 주어진 <code>sources</code>의 원소 순서대로 강철부대로 복귀할 수 있는 최단시간을 담은 배열을 return하는 solution 함수를 완성해주세요. 복귀가 불가능한 경우 해당 부대원의 최단시간은 -1입니다.</p>

<h5>제한사항</h5>

<ul>
<li>3 ≤ <code>n</code> ≤ 100,000

<ul>
<li>각 지역은 정수 1부터 <code>n</code>까지의 번호로 구분됩니다.</li>
</ul></li>
<li>2 ≤ <code>roads</code>의 길이 ≤ 500,000

<ul>
<li><code>roads</code>의 원소의 길이 = 2</li>
<li><code>roads</code>의 원소는 [a, b] 형태로 두 지역 a, b가 서로 왕복할 수 있음을 의미합니다.(1 ≤ a, b ≤ n, a ≠ b)</li>
<li>동일한 정보가 중복해서 주어지지 않습니다.

<ul>
<li>동일한 [a, b]가 중복해서 주어지지 않습니다.</li>
<li>[a, b]가 있다면 [b, a]는 주어지지 않습니다.</li>
</ul></li>
</ul></li>
<li>1 ≤ <code>sources</code>의 길이 ≤ 500

<ul>
<li>1 ≤&nbsp;<code>sources[i]</code>&nbsp;≤ n</li>
</ul></li>
<li>1 ≤ <code>destination</code> ≤ n</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>roads</th>
<th>sources</th>
<th>destination</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>3</td>
<td>[[1, 2], [2, 3]]</td>
<td>[2, 3]</td>
<td>1</td>
<td>[1, 2]</td>
</tr>
<tr>
<td>5</td>
<td>[[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]]</td>
<td>[1, 3, 5]</td>
<td>5</td>
<td>[2, -1, 0]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<ul>
<li>지역 2는 지역 1과 길로 연결되어 있기 때문에, 지역 2에서 지역 1의 최단거리는 1입니다.</li>
<li>지역 3에서 지역 1로 이동할 수 있는 최단경로는 지역 3 → 지역 2 → 지역 1 순으로 이동하는 것이기 때문에, 지역 3에서 지역 1의 최단거리는 2입니다. </li>
<li>따라서 [1, 2]를 return합니다.</li>
</ul>

<p><strong>입출력 예 #2</strong></p>

<ul>
<li>지역 1에서 지역 5의 최단경로는 지역 1 → 지역 2 → 지역 5 또는 지역 1 → 지역 4 → 지역 5 순으로 이동하는 것이기 때문에, 최단거리는 2입니다.</li>
<li>지역 3에서 지역 5로 가는 경로가 없기 때문에, 지역 3에서 지역 5로 가는 최단거리는 -1입니다.</li>
<li>지역 5에서 지역 5는 이동할 필요가 없기 때문에, 최단거리는 0입니다.</li>
<li>따라서 [2, -1, 0]을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges