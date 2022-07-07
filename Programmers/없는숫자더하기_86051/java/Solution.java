package Programmers.없는숫자더하기_86051.java;

public class Solution {
    public int solution(int[] numbers) {
        int answer = 45;
        for (int number : numbers) {
            answer -= number;
        }
        return answer;
    }
}

/**
 * 정확성  테스트
    테스트 1 〉	통과 (0.02ms, 73.9MB)
    테스트 2 〉	통과 (0.02ms, 74MB)
    테스트 3 〉	통과 (0.02ms, 68.8MB)
    테스트 4 〉	통과 (0.02ms, 76.9MB)
    테스트 5 〉	통과 (0.03ms, 77.7MB)
    테스트 6 〉	통과 (0.02ms, 78.5MB)
    테스트 7 〉	통과 (0.02ms, 75.8MB)
    테스트 8 〉	통과 (0.02ms, 84.7MB)
    테스트 9 〉	통과 (0.01ms, 75.5MB)
 */
