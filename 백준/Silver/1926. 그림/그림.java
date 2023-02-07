import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.lang.Math;
import java.util.*;

class Main {
    static int n, m;
    static int [][] maps;
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
        Queue<Point> queue = new LinkedList<Point>();
        queue.offer(start);
        visit[start.x][start.y] = true;
        int cnt = 1;
        while (!queue.isEmpty()) {
            int size = queue.size();

            for (int s = 0; s < size; s++) {
                Point current = queue.poll();

                for (int i = 0; i < 4; i++) {
                    int nx = current.x + dx[i];
                    int ny = current.y + dy[i];

                    if (0 <= nx && nx < n && 0 <= ny && ny < m && !visit[nx][ny] && maps[nx][ny] == 1) { 
                        queue.offer(new Point(nx, ny));
                        visit[nx][ny] = true;
                        cnt += 1;
                    }
                }
            }
        }
        return cnt;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String [] nums = br.readLine().split(" ");

        n = Integer.parseInt(nums[0]);
        m = Integer.parseInt(nums[1]);

        int ans1 = 0;
        int ans2 = 0;

        maps = new int [n][m];
        visit = new boolean [n][m];

        for (int i = 0; i < n; i++) {
            String [] row = br.readLine().split(" ");
            for (int j = 0; j < m; j++) {
                maps[i][j] = Integer.parseInt(row[j]);
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if(!visit[i][j] && maps[i][j] == 1) {
                    int k = BFS(new Point(i, j));
                    
                    ans2 = Math.max(k, ans2);
                    ans1 += 1;
                }
            }
        }
        System.out.println(ans1);
        System.out.println(ans2);
    }
}