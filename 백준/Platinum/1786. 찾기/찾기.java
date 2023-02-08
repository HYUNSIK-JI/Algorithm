import java.io.*;
import java.lang.reflect.Array;
import java.util.*;
import java.lang.*;
 
public class Main {
 
 
 
    static String t;
    static String p;
 
    static int[] table;
    static List<Integer> answers = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 
        t = br.readLine();
        p = br.readLine();
 
        table = new int[p.length()];
 
        solve();
 
        System.out.println(answers.size());
 
        for(Integer answer: answers){
            System.out.println(answer);
        }
    }
 
    private static void solve(){
        makeTable();
 
        int tLength = t.length();
        int pLength = p.length();
 
        int idx = 0;
 
        for(int i = 0; i < tLength; i++){
            while(idx > 0 && t.charAt(i) != p.charAt(idx)){
                idx = table[idx-1];
            }
            if(t.charAt(i) == p.charAt(idx)) {
                if (idx == pLength - 1) {
                    answers.add(i - idx + 1);
                    idx = table[idx];
                } else {
                    idx += 1;
                }
            }
        }
    }
 
    private static void makeTable(){
        int n = p.length();
 
        int idx = 0;
 
        for(int i = 1; i < n; i++){
            while(idx > 0 && p.charAt(i) != p.charAt(idx)){
                idx = table[idx - 1];
            }
 
            if(p.charAt(i) == p.charAt(idx)){
                idx++;
                table[i] = idx;
            }
        }
    }
}