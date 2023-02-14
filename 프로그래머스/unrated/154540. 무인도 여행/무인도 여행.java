import java.util.*;

class Solution {
    static int n, m;
    static char [][] maps;
    static boolean [][] visit;
    static int [] dx = {0, 0, 1, -1};
    static int [] dy = {1, -1, 0, 0};
    public static class Point {
        int x, y;
        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    public static int BFS(Point start) {
        visit[start.x][start.y] = true;
        Queue<Point> queue = new LinkedList<Point>();
        queue.offer(start);
        int sum = Character.getNumericValue(maps[start.x][start.y]);
        while (!queue.isEmpty()) {
            Point current = queue.poll();
            
            for (int i = 0; i < 4; i++) {
                int nx = current.x + dx[i];
                int ny = current.y + dy[i];
                
                if (0 <= nx && nx < n && 0 <= ny && ny < m && !visit[nx][ny]) {
                    if (maps[nx][ny] != 'X') {
                        visit[nx][ny] = true;
                        sum += Character.getNumericValue(maps[nx][ny]);
                        queue.offer(new Point(nx, ny));
                    }
                }
            }
        }
        return sum;
    }
    public int[] solution(String[] graph) {
        n = graph.length;
        m = graph[0].length();
        
        maps = new char [n][m];
        visit = new boolean [n][m];
        int land = 0;
        ArrayList<Integer> ans = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            char [] row = graph[i].toCharArray();
            for (int j = 0; j < m; j++) {
                maps[i][j] = row[j];
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (maps[i][j] != 'X' && !visit[i][j]) {
                    ans.add(BFS(new Point(i, j)));
                    land += 1;
                    
                }
            }
        }
        
        if (land == 0) {
            int [] answer = new int [land + 1];
            answer[0] = -1;
            return answer;
        }
        else {
            int [] answer = new int [land];
            
            for (int i: ans) {
                answer[land - 1] = i;
                land -= 1;
            }
            Arrays.sort(answer);
            return answer;
        }
    }
}