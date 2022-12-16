import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static void bs(int target, int start, int end, int[] arr) {
        int mid;
        if (start <= end) {
            mid = (start + end) / 2;
            if (target == arr[mid]) System.out.println(1);
            else if (target < arr[mid]) bs(target, start, mid - 1, arr);
            else bs(target, mid + 1, end, arr);
        }
        else System.out.println(0);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String[] S = br.readLine().split(" ");

        int[] s = new int[n];

        for (int i=0; i < n; i++) s[i] = Integer.parseInt(S[i]);

        Arrays.sort(s);

        int m = Integer.parseInt(br.readLine());
        String[] F = br.readLine().split(" ");

        for (int i=0; i < m ; i++) bs(Integer.parseInt(F[i]), 0, n - 1, s);
    }
}