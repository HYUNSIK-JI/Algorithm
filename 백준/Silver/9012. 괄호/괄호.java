import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            Stack<Character> stk = new Stack<>();

            for (int j = 0; j < s.length(); j++) {
                char ch = s.charAt(j);

                if (ch == '(') {
                    stk.push(ch);
                }
                else {
                    int size = stk.size();
                    if (size == 0) {
                        stk.push(ch);
                        break;
                    }
                    else {
                        stk.pop();
                    }
                }
            }
            if(stk.isEmpty()) {
				System.out.println("YES");
			}
			else {
				System.out.println("NO");
			}

			stk.clear();
        }
    }
}