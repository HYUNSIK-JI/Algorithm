import java.io.*;
import java.util.*;

class Main {
    static int n;
    static int [][] maps;
    static int [][] visit;
    static int [] dx = {0, 0, 1, -1};
    static int [] dy = {1, -1, 0, 0};
    public static class Point {
        int x, y;
        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    private static void BFS(Point start) {
        visit[start.x][start.y] = 1;
        Deque<Point> queue = new LinkedList<Point>();
        queue.offer(start);

        while (!queue.isEmpty()) {
            int size = queue.size();

            for (int s = 0; s < size; s++) {
                Point current = queue.poll();

                for (int i = 0; i < 4; i++) {
                    int nx = current.x + dx[i];
                    int ny = current.y + dy[i];

                    if (0 <= nx && nx < n && 0 <= ny && ny < n && visit[nx][ny] == 0) {
                        if (maps[nx][ny] == 1) {
                            queue.offerFirst(new Point(nx, ny));
                            visit[nx][ny] = visit[current.x][current.y];
                        }
                        else {
                            queue.offer(new Point(nx, ny));
                            visit[nx][ny] = visit[current.x][current.y] + 1;
                        }
                    }
                }
            }
        }

    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        visit = new int [n][n];
        maps = new int [n][n];
        
        for (int i = 0; i < n; i++) {
            String [] row = br.readLine().split("");
            for (int j = 0; j < n; j++) {
                maps[i][j] = Integer.parseInt(row[j]);
            }
        }

        BFS(new Point(0, 0));
        System.out.println(visit[n - 1][n - 1] - 1);
    }
}