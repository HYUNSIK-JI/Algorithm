import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.lang.Math;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String [] nums = br.readLine().split(" ");
        int [] ans = new int[n];

        for (int i=0; i < n; i++) {
            ans[i] = Integer.parseInt(nums[i]);
        }
        int left = 0;
        int right = 0;
        int answer = 0;

        for (int i = 0; i < n; i++) {
            if (ans[i] == 1) {
                left += 1;
                right -= 1;
            }
            else {
                left -= 1;
                right += 1;
            }
            left = Math.max(left, 0);
            right = Math.max(right, 0);
            answer = Math.max(answer, Math.abs(left - right));
        }
        System.out.println(answer);
    }
}