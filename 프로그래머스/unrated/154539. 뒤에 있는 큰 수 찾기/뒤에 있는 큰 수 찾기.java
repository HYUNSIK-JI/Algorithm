import java.util.*;

class Solution {
    public static class Point {
        int x, y;
        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    public int[] solution(int[] numbers) {
        int [] ans = new int [numbers.length];
        for (int i = 0; i < ans.length; i++) {
            ans[i] = -1;
        }
        Stack<Point> stack = new Stack<Point>();
        int y = -1;
        for(int i : numbers) {
            y += 1;
            while (!stack.empty()) {
                Point current = stack.pop();
                if (current.x < i) {
                    ans[current.y] = i;
                }
                else {
                    stack.push(current);
                    break;
                }
            }
            stack.push(new Point(i, y));
        }
        return ans;
    }
}