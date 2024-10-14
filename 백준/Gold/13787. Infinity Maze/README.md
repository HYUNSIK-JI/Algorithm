# [Gold II] Infinity Maze - 13787 

[문제 링크](https://www.acmicpc.net/problem/13787) 

### 성능 요약

메모리: 130244 KB, 시간: 176 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2024년 10월 14일 17:37:10

### 문제 설명

<p>Dr. Fukuoka has placed a simple robot in a two-dimensional maze. It moves within the maze and never goes out of the maze as there is no exit.</p>

<p>The maze is made up of H × W grid cells as depicted below. The upper side of the maze faces north. Consequently, the right, lower and left sides face east, south and west respectively. Each cell is either empty or wall and has the coordinates of (i, j) where the north-west corner has (1, 1). The row i goes up toward the south and the column j toward the east. </p>

<p><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/13787/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202016-12-26%20%EC%98%A4%ED%9B%84%204.02.58.png" style="height:226px; width:313px"></p>

<p>The robot moves on empty cells and faces north, east, south or west. It goes forward when there is an empty cell in front, and rotates 90 degrees to the right when it comes in front of a wall cell or on the edge of the maze. It cannot enter the wall cells. It stops right after moving forward by L cells.</p>

<p>Your mission is, given the initial position and direction of the robot and the number of steps, to write a program to calculate the final position and direction of the robot.</p>

### 입력 

 <p>The input is a sequence of datasets. Each dataset is formatted as follows.</p>

<pre><code>H W L
c<sub>1,1</sub>c<sub>1,2</sub> . . . c<sub>1,W
</sub>. 
. 
. 
c<sub>H,1</sub>c<sub>H,2</sub> . . . c<sub>H,W </sub></code></pre>

<p>The first line of a dataset contains three integers H, W and L(1 ≤ H, W ≤ 100, 1 ≤ L ≤ 10<sup>18</sup>).</p>

<p>Each of the following H lines contains exactly W characters. In the i-th line, the j-th character ci,j represents a cell at (i, j) of the maze. “.” denotes an empty cell. “#” denotes a wall cell. “N”, “E”, “S”, “W” denote a robot on an empty cell facing north, east, south and west respectively; it indicates the initial position and direction of the robot.</p>

<p>You can assume that there is at least one empty cell adjacent to the initial position of the robot.</p>

<p>The end of input is indicated by a line with three zeros. This line is not part of any dataset.</p>

### 출력 

 <p>For each dataset, output in a line the final row, column and direction of the robot, separated by a single space. The direction should be one of the following: “N” (north), “E” (east), “S” (south) and “W” (west).</p>

<p>No extra spaces or characters are allowed.</p>

