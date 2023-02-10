import java.io.*;
import java.util.*;

class Main {
    static int r, c;
    static char [][] maps;
    static Queue<Point> Fire = new LinkedList<Point>();
    static Queue<Point> queue = new LinkedList<Point>();
    static int [] dx = {0, 0, 1, -1};
    static int [] dy = {1, -1, 0, 0};

    public static class Point {
        int x, y, cnt;
        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
        public Point(int x, int y, int cnt) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
        }
    }

    public static int BFS() {
        while (!queue.isEmpty()) {
            int fsize = Fire.size();

            for (int s = 0; s < fsize; s++) {
                Point fcurrent = Fire.poll();

                for (int i = 0; i < 4; i++) {
                    int nx = fcurrent.x + dx[i];
                    int ny = fcurrent.y + dy[i];

                    if (0 <= nx && nx < r && 0 <= ny && ny < c && maps[nx][ny] == '.') {
                        maps[nx][ny] = 'F';
                        Fire.offer(new Point(nx, ny));
                    }
                }
            }

            int size = queue.size();

            for (int s = 0; s < size; s++) {
                Point current = queue.poll();

                for (int i = 0; i < 4; i++) {
                    int nx = current.x + dx[i];
                    int ny = current.y + dy[i];

                    if (0 <= nx && nx < r && 0 <= ny && ny < c) {
                        if (maps[nx][ny] == '.') {
                            maps[nx][ny] = 'J';
                            queue.offer(new Point(nx, ny, current.cnt + 1));
                        }
                    }
                    else {
                        return current.cnt + 1;
                    }
                }
            }
        }
        return -1;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String [] nums = br.readLine().split(" ");
        
        r = Integer.parseInt(nums[0]);
        c = Integer.parseInt(nums[1]);

        maps = new char [r][c];

        for (int i = 0; i < r; i++) {
            char [] row = br.readLine().toCharArray();
            for (int j = 0; j < c; j++) {
                maps[i][j] = row[j];

                if (maps[i][j] == 'J') queue.offer(new Point(i, j, 0));
                if (maps[i][j] == 'F') Fire.offer(new Point(i, j));
            }
        }

        int ans = BFS();
        if (ans == -1) System.out.println("IMPOSSIBLE");
        else System.out.println(ans);
    }
}