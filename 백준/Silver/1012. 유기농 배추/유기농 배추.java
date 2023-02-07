import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

class Main {
    static int t;
    static int m, n, k;
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

    public static void BFS(Point start) {
        Queue<Point> queue = new LinkedList<Point>();
        queue.offer(start);
        visit[start.x][start.y] = true;

        while(!queue.isEmpty()) {
            int size = queue.size();

            for (int s = 0; s < size; s++) {
                Point current = queue.poll();

                for (int i = 0; i < 4; i++) {
                    int nx = current.x + dx[i];
                    int ny = current.y + dy[i];

                    if (0 <= nx && nx < n && 0 <= ny && ny < m && !visit[nx][ny] && maps[nx][ny] == 1) {
                        queue.offer(new Point(nx, ny));
                        visit[nx][ny] = true;
                    }
                }
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        

        t = Integer.parseInt(br.readLine());
        
        for (int test = 0; test < t; test++) {
            String [] nums = br.readLine().split(" ");

            m = Integer.parseInt(nums[1]);
            n = Integer.parseInt(nums[0]);
            k = Integer.parseInt(nums[2]);

            maps = new int [n][m];
            visit = new boolean [n][m];

            int answer = 0;
            for (int i = 0; i < k; i++) {
                String [] position = br.readLine().split(" ");
                int a = Integer.parseInt(position[0]);
                int b = Integer.parseInt(position[1]);
                maps[a][b] = 1;
            }

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if(!visit[i][j] && maps[i][j] == 1) { 
                        BFS(new Point(i, j));
                        answer += 1;
                    }
                }
            }
            System.out.println(answer);
        }
    }
    
}