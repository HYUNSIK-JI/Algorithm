import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        ArrayList<Integer> ans = new ArrayList<>();

        for (int i = 0; i < n; i++) ans.add(Integer.parseInt(br.readLine()));

        Collections.sort(ans);
        for (int num: ans) sb.append(num).append("\n");

        System.out.println(sb);
    }
}