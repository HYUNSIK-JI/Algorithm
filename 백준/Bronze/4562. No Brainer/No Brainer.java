import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String len = br.readLine();
        for (int i = 0; i < Integer.parseInt(len); i++) {
            String[] input = br.readLine().split(" ");
            
            int a = Integer.parseInt(input[0]);
            int b = Integer.parseInt(input[1]);
            
            if (a < b) System.out.println("NO BRAINS");
            else System.out.println("MMM BRAINS");
        }
    }
}