import java.io.*;
import java.util.*;

class Main {
    static int n;
    static Character [][] maps;
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

        char color = maps[start.x][start.y];

        while (!queue.isEmpty()) {
            int size = queue.size();
            
            for (int s = 0; s < size; s++) {
                Point current = queue.poll();

                for (int i = 0; i < 4; i++) {
                    int nx = current.x + dx[i];
                    int ny = current.y + dy[i];

                    if (0 <= nx && nx < n && 0 <= ny && ny < n && !visit[nx][ny] && color == maps[nx][ny]) {
                        visit[nx][ny] = true;
                        queue.offer(new Point(nx, ny));
                    }
                    
                }
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        Queue<Point> colors = new LinkedList<Point>();
        maps = new Character [n][n];
        visit = new boolean [n][n];
        String g = "G";
        char gg = g.charAt(0);
        int ans1 = 0;
        int ans2 = 0;

        for (int i = 0; i < n; i++) {
            String row = br.readLine();
            for (int j = 0; j < n; j++) {
                maps[i][j] = row.charAt(j);
                if (maps[i][j] == gg) colors.offer(new Point(i, j));
            }
        }
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visit[i][j]) {
                    BFS(new Point(i, j));
                    ans1 += 1;
                }
            }
        }
        while (!colors.isEmpty()) {
            int color_size = colors.size();

            for (int s = 0; s < color_size; s++) {
                Point c = colors.poll();
                String r = "R";
                maps[c.x][c.y] = r.charAt(0);
            }
        }
        visit = new boolean [n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if(!visit[i][j]) {
                    BFS(new Point(i, j));
                    ans2 += 1;
                }
            }
        }
        System.out.println(ans1);
        System.out.println(ans2);
    }
}