import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

import java.util.*;

class Main {
    static int n, m;
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
    public static int count(Point start) {
        int cnt = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cnt += maps[i][j];
            }
        }

        return cnt;
    }

    public static void BFS(Point start) {
        Queue<Point> queue = new LinkedList<Point>();
        queue.offer(start);

        visit[start.x][start.y] = 1;

        while (!queue.isEmpty()) {
            int size = queue.size();

            for (int s = 0; s < size; s++) {
                Point current = queue.poll();

                for (int i = 0; i < 4; i++) {
                    int nx = current.x + dx[i];
                    int ny = current.y + dy[i];

                    if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                        if (visit[nx][ny] == 0) {
                            if (maps[nx][ny] == 0) {
                                queue.offer(new Point(nx, ny));
                            }
                            visit[nx][ny] += 1;
                        }
                    }
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (maps[i][j] >= 1 && visit[i][j] >= 1) {
                    maps[i][j] = 0;
                }
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String [] nums = br.readLine().split(" ");

        n = Integer.parseInt(nums[0]);
        m = Integer.parseInt(nums[1]);

        maps = new int [n][m];
        

        for (int i = 0; i < n; i++) {
            String [] row = br.readLine().split(" ");
            for (int j = 0; j < m; j++) {
                maps[i][j] = Integer.parseInt(row[j]);
            }
        }

        int cheeze = 0;
        int time = 0;

        while (true) {

            int c = count(new Point(0, 0));
            if (c == 0) break;

            visit = new int [n][m];
            BFS(new Point(0, 0));
            time += 1;

            cheeze = c;
        }
        System.out.println(time);
        System.out.println(cheeze);
    }
}