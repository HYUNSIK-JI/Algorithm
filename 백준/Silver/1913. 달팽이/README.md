# [Silver III] 달팽이 - 1913 

[문제 링크](https://www.acmicpc.net/problem/1913) 

### 성능 요약

메모리: 124596 KB, 시간: 304 ms

### 분류

구현(implementation)

### 문제 설명

<p>홀수인 자연수 N이 주어지면, 다음과 같이 1부터 N<sup>2</sup>까지의 자연수를 달팽이 모양으로 N×N의 표에 채울 수 있다.</p>

<table class="table table-bordered td-center" style="width:9%">
	<tbody>
		<tr>
			<td style="width:3%">9</td>
			<td style="width:3%">2</td>
			<td style="width:3%">3</td>
		</tr>
		<tr>
			<td>8</td>
			<td>1</td>
			<td>4</td>
		</tr>
		<tr>
			<td>7</td>
			<td>6</td>
			<td>5</td>
		</tr>
	</tbody>
</table>

<table class="table table-bordered td-center" style="width:15%">
	<tbody>
		<tr>
			<td style="width:3%">25</td>
			<td style="width:3%">10</td>
			<td style="width:3%">11</td>
			<td style="width:3%">12</td>
			<td style="width:3%">13</td>
		</tr>
		<tr>
			<td>24</td>
			<td>9</td>
			<td>2</td>
			<td>3</td>
			<td>14</td>
		</tr>
		<tr>
			<td>23</td>
			<td>8</td>
			<td>1</td>
			<td>4</td>
			<td>15</td>
		</tr>
		<tr>
			<td>22</td>
			<td>7</td>
			<td>6</td>
			<td>5</td>
			<td>16</td>
		</tr>
		<tr>
			<td>21</td>
			<td>20</td>
			<td>19</td>
			<td>18</td>
			<td>17</td>
		</tr>
	</tbody>
</table>

<p>N이 주어졌을 때, 이러한 표를 출력하는 프로그램을 작성하시오. 또한 N<sup>2</sup> 이하의 자연수가 하나 주어졌을 때, 그 좌표도 함께 출력하시오. 예를 들어 N=5인 경우 6의 좌표는 (4,3)이다.</p>

### 입력 

 <p>첫째 줄에 홀수인 자연수 N(3 ≤ N ≤ 999)이 주어진다. 둘째 줄에는 위치를 찾고자 하는 N<sup>2</sup> 이하의 자연수가 하나 주어진다.</p>

### 출력 

 <p>N개의 줄에 걸쳐 표를 출력한다. 각 줄에 N개의 자연수를 한 칸씩 띄어서 출력하면 되며, 자릿수를 맞출 필요가 없다. N+1번째 줄에는 입력받은 자연수의 좌표를 나타내는 두 정수를 한 칸 띄어서 출력한다.</p>

