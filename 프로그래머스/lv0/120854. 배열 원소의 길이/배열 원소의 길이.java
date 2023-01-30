
class Solution {
    public int[] solution(String[] strlist) {
        int n = strlist.length;
        int[] answer = new int [n];
        for(int i = 0; i < n; i++) {
            answer[i] = strlist[i].length();
        }
        return answer;
    }
}