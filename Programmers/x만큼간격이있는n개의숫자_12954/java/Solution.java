package Programmers.x만큼간격이있는n개의숫자_12954.java;

public class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        for (int i=0; i<n; i++) {
            answer[i] = (long) x*(i+1);    
        }
        return answer;
    }
}

/**
 * 7번 라인에서 형변환 안 하면 테스트 9, 10 틀림
 * 10000000 * 1000의 경우, int 최대 범위 초과
 */

/**
 * 정확성  테스트
    테스트 1 〉	통과 (0.02ms, 74.6MB)
    테스트 2 〉	통과 (0.01ms, 82.5MB)
    테스트 3 〉	통과 (0.03ms, 84.6MB)
    테스트 4 〉	통과 (0.03ms, 76.7MB)
    테스트 5 〉	통과 (0.03ms, 79.6MB)
    테스트 6 〉	통과 (0.02ms, 77.6MB)
    테스트 7 〉	통과 (0.05ms, 76.7MB)
    테스트 8 〉	통과 (0.02ms, 77.5MB)
    테스트 9 〉	통과 (0.04ms, 75.1MB)
    테스트 10 〉	통과 (0.01ms, 74.4MB)
    테스트 11 〉	통과 (0.02ms, 75MB)
    테스트 12 〉	통과 (0.03ms, 76.7MB)
    테스트 13 〉	통과 (0.04ms, 74.1MB)
    테스트 14 〉	통과 (0.04ms, 78.6MB)
 */