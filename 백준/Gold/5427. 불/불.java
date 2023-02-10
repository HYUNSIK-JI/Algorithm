import java.io.*;
import java.util.*;

class Main {
    static int h, w;
    static Character [][] maps;
    static int [][] visit;
    static int dx [] = {0, 0, 1, -1};
    static int dy [] = {1, -1, 0, 0};
    static Queue<Point> Fire = new LinkedList<>();

    public static class Point {
        int x, y, c;
        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
        public Point(int x, int y, int c) {
            this.x = x;
            this.y = y;
            this.c = c;
        }
    }

    public static int BFS(Point start) {
        Queue<Point> queue = new LinkedList<Point>();
        visit[start.x][start.y] = 0;
        
        queue.offer(start);
        while (!queue.isEmpty()) {
            
            int firesize = Fire.size();
            for (int fs = 0; fs < firesize; fs++) {
                Point fcurrent = Fire.poll();

                for (int i = 0; i < 4; i++) {
                    int nx = fcurrent.x + dx[i];
                    int ny = fcurrent.y + dy[i];

                    if (0 <= nx && nx < h && 0 <= ny && ny < w && maps[nx][ny] == '.') {
                        maps[nx][ny] = '*';
                        
                        Fire.offer(new Point(nx, ny));
                    }
                }
            }

            int qsize = queue.size();
            for (int s = 0; s < qsize; s++) {
                Point current = queue.poll();

                for (int i = 0; i < 4; i++) {
                    int nx = current.x + dx[i];
                    int ny = current.y + dy[i];

                    if (0 <= nx && nx < h && 0 <= ny && ny < w){
                        if (maps[nx][ny] == '.') {
                            maps[nx][ny] = '@';
                            visit[nx][ny] = visit[current.x][current.y] + 1;
                            queue.offer(new Point(nx, ny));
                        }
                    }
                    else {
                        return visit[current.x][current.y] + 1;
                    }
                }
            }
        }
        return -1;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for(int k = 0; k < n; k++) {
            String [] nums = br.readLine().split(" ");

            h = Integer.parseInt(nums[1]);
            w = Integer.parseInt(nums[0]);

            maps = new Character [h][w];
            visit = new int [h][w];
            Fire = new LinkedList<Point>();

            int s_x = 0;
            int s_y = 0;
            for (int i = 0; i < h; i++) {
                String row = br.readLine();
                for (int j = 0; j < w; j++) {
                    maps[i][j] = row.charAt(j);
                    if (maps[i][j] == '@') {
                        s_x = i;
                        s_y = j;
                    }
                    if (maps[i][j] == '*') {
                        Fire.offer(new Point(i, j));
                    }
                }
            }
            int ans = BFS(new Point(s_x, s_y, 0));
            if (ans == -1) System.out.println("IMPOSSIBLE");
            else System.out.println(ans);
        }
    }
}