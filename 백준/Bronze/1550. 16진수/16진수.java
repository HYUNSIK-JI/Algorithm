import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        
        String hx = in.readLine();
        
        int answer = Integer.parseInt(hx, 16);
        String ans = Integer.toString(answer);
        
        out.append(ans);
        out.close();
    }
}