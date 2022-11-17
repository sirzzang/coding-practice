package Programmers.햄버거만들기_133502.java;

public class Solution2 {
    public int solution(int[] ingredient) {
        int answer = 0;
        String burger = "1231";
        
        StringBuilder sb = new StringBuilder();
        for (int i: ingredient) {
            sb.append(String.valueOf(i));
            
            int index = sb.indexOf(burger);
            if (index >= 0) {
                answer++;
                sb.delete(index, index+4);
            }            
            
        }   
        
        return answer;
    }
}
