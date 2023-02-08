import java.io.*;
import java.util.*;

class Main {
    static int n;
    public static int [] ans;
    public static boolean [] visit;
    public static ArrayList<Integer>[] maps;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        maps = new ArrayList[n + 1];
        visit = new boolean[n + 2];
        ans = new int [n + 2];

        for (int i = 1; i < n + 1; i++) {
            maps[i] = new ArrayList<Integer>();
        }

        for (int i = 0; i < n - 1; i++) {
            String [] nums = br.readLine().split(" ");
            int a = Integer.parseInt(nums[0]);
            int b = Integer.parseInt(nums[1]);

            maps[a].add(b);
            maps[b].add(a);
        }
        DFS(1);

        for (int i = 2; i < n + 1; i++) System.out.println(ans[i]);
    }
    private static void DFS(int start) {
        visit[start] = true;
        
        for (int i: maps[start]) {
            if (!visit[i]) {
                ans[i] = start;
                DFS(i);
            }
        }
    }
}