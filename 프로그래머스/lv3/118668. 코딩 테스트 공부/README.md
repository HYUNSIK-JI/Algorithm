# [level 3] 코딩 테스트 공부 - 118668 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/118668) 

### 성능 요약

메모리: 10.3 MB, 시간: 4.52 ms

### 구분

코딩테스트 연습 > 2022 KAKAO TECH INTERNSHIP

### 채점결과

<br/>정확성: 50.0<br/>효율성: 50.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p><strong>[본 문제는 정확성과 효율성 테스트 각각 점수가 있는 문제입니다.]</strong></p>

<p>당신은 코딩 테스트를 준비하기 위해 공부하려고 합니다. 코딩 테스트 문제를 풀기 위해서는 알고리즘에 대한 지식과 코드를 구현하는 능력이 필요합니다.</p>

<p>알고리즘에 대한 지식은 <code>알고력</code>, 코드를 구현하는 능력은 <code>코딩력</code>이라고 표현합니다. <code>알고력</code>과 <code>코딩력</code>은 0 이상의 정수로 표현됩니다.</p>

<p>문제를 풀기 위해서는 문제가 요구하는 일정 이상의 <code>알고력</code>과 <code>코딩력</code>이 필요합니다.</p>

<p>예를 들어, 당신의 현재 <code>알고력</code>이 15, <code>코딩력</code>이 10이라고 가정해보겠습니다.</p>

<ul>
<li>A라는 문제가 <code>알고력</code> 10, <code>코딩력</code> 10을 요구한다면 A 문제를 풀 수 있습니다.</li>
<li>B라는 문제가 <code>알고력</code> 10, <code>코딩력</code> 20을 요구한다면 <code>코딩력</code>이 부족하기 때문에 B 문제를 풀 수 없습니다.</li>
</ul>

<p>풀 수 없는 문제를 해결하기 위해서는 <code>알고력</code>과 <code>코딩력</code>을 높여야 합니다. <code>알고력</code>과 <code>코딩력</code>을 높이기 위한 다음과 같은 방법들이 있습니다.</p>

<ul>
<li><code>알고력</code>을 높이기 위해 알고리즘 공부를 합니다. <code>알고력</code> 1을 높이기 위해서 1의 시간이 필요합니다.</li>
<li><code>코딩력</code>을 높이기 위해 코딩 공부를 합니다. <code>코딩력</code> 1을 높이기 위해서 1의 시간이 필요합니다.</li>
<li>현재 풀 수 있는 문제 중 하나를 풀어 <code>알고력</code>과 <code>코딩력</code>을 높입니다. 각 문제마다 문제를 풀면 올라가는 알고력과 코딩력이 정해져 있습니다.</li>
<li>문제를 하나 푸는 데는 문제가 요구하는 시간이 필요하며 같은 문제를 여러 번 푸는 것이 가능합니다.</li>
</ul>

<p>당신은 주어진 모든 문제들을 풀 수 있는 <code>알고력</code>과 <code>코딩력</code>을 얻는 최단시간을 구하려 합니다.</p>

<p>초기의 <code>알고력</code>과 <code>코딩력</code>을 담은 정수 <code>alp</code>와 <code>cop</code>, 문제의 정보를 담은 2차원 정수 배열 <code>problems</code>가 매개변수로 주어졌을 때, 모든 문제들을 풀 수 있는 <code>알고력</code>과 <code>코딩력</code>을 얻는 최단시간을 return 하도록 solution 함수를 작성해주세요.</p>

<p><strong>모든 문제들을 1번 이상씩 풀 필요는 없습니다.  <code>입출력 예 설명</code>을 참고해주세요.</strong></p>

<hr>

<h5>제한사항</h5>

<ul>
<li>초기의 <code>알고력</code>을 나타내는 <code>alp</code>와 초기의 <code>코딩력</code>을 나타내는 <code>cop</code>가 입력으로 주어집니다.

<ul>
<li>0 ≤ <code>alp</code>,<code>cop</code> ≤ 150</li>
</ul></li>
<li>1 ≤ <code>problems</code>의 길이 ≤ 100</li>
<li><code>problems</code>의 원소는 [<code>alp_req</code>, <code>cop_req</code>, <code>alp_rwd</code>, <code>cop_rwd</code>, <code>cost</code>]의 형태로 이루어져 있습니다.</li>
<li><code>alp_req</code>는 문제를 푸는데 필요한 <code>알고력</code>입니다.

<ul>
<li>0 ≤ <code>alp_req</code> ≤ 150</li>
</ul></li>
<li><code>cop_req</code>는 문제를 푸는데 필요한 <code>코딩력</code>입니다.

<ul>
<li>0 ≤ <code>cop_req</code> ≤ 150</li>
</ul></li>
<li><code>alp_rwd</code>는 문제를 풀었을 때 증가하는 <code>알고력</code>입니다.

<ul>
<li>0 ≤ <code>alp_rwd</code> ≤ 30</li>
</ul></li>
<li><code>cop_rwd</code>는 문제를 풀었을 때 증가하는 <code>코딩력</code>입니다.

<ul>
<li>0 ≤ <code>cop_rwd</code> ≤ 30</li>
</ul></li>
<li><code>cost</code>는 문제를 푸는데 드는 시간입니다.

<ul>
<li>1 ≤ <code>cost</code> ≤ 100</li>
</ul></li>
</ul>

<p><strong>정확성 테스트 케이스 제한사항</strong></p>

<ul>
<li>0 ≤ <code>alp</code>,<code>cop</code> ≤ 20</li>
<li>1 ≤ <code>problems</code>의 길이 ≤ 6

<ul>
<li>0 ≤ <code>alp_req</code>,<code>cop_req</code> ≤ 20</li>
<li>0 ≤ <code>alp_rwd</code>,<code>cop_rwd</code> ≤ 5</li>
<li>1 ≤ <code>cost</code> ≤ 10</li>
</ul></li>
</ul>

<p><strong>효율성 테스트 케이스 제한사항</strong></p>

<ul>
<li>주어진 조건 외 추가 제한사항 없습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>alp</th>
<th>cop</th>
<th>problems</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>10</td>
<td>10</td>
<td>[[10,15,2,1,2],[20,20,3,3,4]]</td>
<td>15</td>
</tr>
<tr>
<td>0</td>
<td>0</td>
<td>[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]</td>
<td>13</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<ol>
<li><code>코딩력</code> 5를 늘립니다. <code>알고력</code> 10, <code>코딩력</code> 15가 되며 시간이 5만큼 소요됩니다.</li>
<li>1번 문제를 5번 풉니다. <code>알고력</code> 20, <code>코딩력</code> 20이 되며 시간이 10만큼 소요됩니다.
15의 시간을 소요하여 모든 문제를 풀 수 있는 <code>알고력</code>과 <code>코딩력</code>을 가질 수 있습니다.</li>
</ol>

<p><strong>입출력 예 #2</strong></p>

<ol>
<li>1번 문제를 2번 풉니다. <code>알고력</code>&nbsp;4, <code>코딩력</code>&nbsp;2가 되며 시간이 4만큼 소요됩니다.</li>
<li><code>코딩력</code>&nbsp;3을 늘립니다. <code>알고력</code>&nbsp;4, <code>코딩력</code>&nbsp;5가 되며 시간이 3만큼 소요됩니다.</li>
<li>2번 문제를 2번 풉니다. <code>알고력</code> 10, <code>코딩력</code>&nbsp;7이 되며 시간이 4만큼 소요됩니다.</li>
<li>4번 문제를 1번 풉니다. <code>알고력</code> 10, <code>코딩력</code> 11이 되며 시간이 2만큼 소요됩니다.
13의 시간을 소요하여 모든 문제를 풀 수 있는 <code>알고력</code>과 <code>코딩력</code>을 가질 수 있습니다.</li>
</ol>

<hr>

<p><strong>제한시간 안내</strong></p>

<ul>
<li>정확성 테스트 : 10초</li>
<li>효율성 테스트 : 언어별로 작성된 정답 코드의 실행 시간의 적정 배수</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges