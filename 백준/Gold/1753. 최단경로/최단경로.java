import java.io.*;
import java.util.*;

class Main {
    public static class Point {
        int idx, cost;
        public Point(int idx, int cost) {
            this.idx = idx;
            this.cost = cost;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String [] nums = br.readLine().split(" ");

        int v = Integer.parseInt(nums[0]);
        int e = Integer.parseInt(nums[1]);

        int start = Integer.parseInt(br.readLine());

        ArrayList<ArrayList<Point>> maps = new ArrayList<ArrayList<Point>>();

        for (int i = 0; i < v + 1; i++) maps.add(new ArrayList<>());

        for (int i = 0; i < e; i++) {
            String [] num = br.readLine().split(" ");

            int a = Integer.parseInt(num[0]);
            int b = Integer.parseInt(num[1]);
            int c = Integer.parseInt(num[2]);

            maps.get(a).add(new Point(b, c));
        }
        boolean [] visit = new boolean[v + 1];
        int [] dist = new int[v + 1];
        for (int i = 0; i < v + 1; i++) dist[i] = Integer.MAX_VALUE;

        dist[start] = 0;

        for (int i = 0; i < v; i++) {
            int nodevalue = Integer.MAX_VALUE;
            int nodeindex = 0;

            for (int j = 1; j < v + 1; j++) {
                if (!visit[j] && dist[j] < nodevalue) {
                    nodevalue = dist[j];
                    nodeindex = j;
                }
            }

            visit[nodeindex] = true;

            for (int j = 0; j < maps.get(nodeindex).size(); j++) {
                Point adjnode = maps.get(nodeindex).get(j);

                int cost = dist[nodeindex] + adjnode.cost;

                if (cost < dist[adjnode.idx]) {
                    dist[adjnode.idx] = cost;
                }
            }
        }

        for (int i = 1; i < v + 1; i++) {
            if (dist[i] == Integer.MAX_VALUE) System.out.println("INF");
            else System.out.println(dist[i]);
        }
    }
}