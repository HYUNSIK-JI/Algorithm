import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String [] arr = br.readLine().split(" ");

        int n = Integer.parseInt(arr[0]);
        int k = Integer.parseInt(arr[1]);

        ArrayList<Integer> ans = new ArrayList<>();

        String [] nums = br.readLine().split(" ");

        for (int i = 0; i < n; i++) ans.add(Integer.parseInt(nums[i]));
        
        Collections.sort(ans);

        System.out.println(ans.get(k - 1));
    }
}