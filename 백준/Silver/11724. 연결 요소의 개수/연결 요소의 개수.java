import java.io.*;
import java.util.*;

class Main {
    static int n, m;
    public static ArrayList<Integer>[] maps;
    public static boolean[] visit;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String [] nums = br.readLine().split(" ");
        
        n = Integer.parseInt(nums[0]);
        m = Integer.parseInt(nums[1]);

        maps = new ArrayList[n];
        visit = new boolean[n];
        int ans = 0;
        for (int i = 0; i < n; i++) {
            maps[i] = new ArrayList<Integer>();
        }

        for (int i = 0; i < m; i++) {
            String [] num = br.readLine().split(" ");
            int a = Integer.parseInt(num[0]);
            int b = Integer.parseInt(num[1]);

            maps[a - 1].add(b - 1);
            maps[b - 1].add(a - 1);
        }

        for(int i = 0; i < n; i++) {
            if(!visit[i]) {
                DFS(i);
                ans += 1;
            }
        }
        System.out.println(ans);
    }
    private static void DFS(int start) {
        visit[start] = true;

        for(int i: maps[start]) {
            if (!visit[i]) {
                DFS(i);
            }
        }
    }
}