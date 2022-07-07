package Programmers.내적_70128.java;

public class Solution {
    public int solution(int[] a, int[] b) {
        int answer = 0;
        for (int i = 0; i < a.length; i++) {
            answer += a[i] * b[i];
        }
        return answer;
    }    
}

/**
 * 정확성  테스트
    테스트 1 〉	통과 (0.04ms, 72.4MB)
    테스트 2 〉	통과 (0.01ms, 75.7MB)
    테스트 3 〉	통과 (0.02ms, 74.4MB)
    테스트 4 〉	통과 (0.02ms, 76.9MB)
    테스트 5 〉	통과 (0.02ms, 82.9MB)
    테스트 6 〉	통과 (0.02ms, 76.9MB)
    테스트 7 〉	통과 (0.03ms, 66MB)
    테스트 8 〉	통과 (0.03ms, 75.4MB)
    테스트 9 〉	통과 (0.03ms, 77.9MB)
 */
