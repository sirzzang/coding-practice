package Programmers.약수의개수와덧셈_77884.java;

class Solution {
    public int solution(int left, int right) {
        if (left == right) {
            return 0;
        }
        
        int answer = 0;
        
        for (int n = left; n <= right; n++) {
            double sqrt = Math.sqrt(n);
            if (sqrt == (int) sqrt) {
                answer -= n;
            } else {
                answer += n;
            }
        }
        
        return answer;
    }
}

/**
 * 정확성  테스트
    테스트 1 〉	통과 (0.07ms, 78.7MB)
    테스트 2 〉	통과 (0.10ms, 74.2MB)
    테스트 3 〉	통과 (0.03ms, 75.5MB)
    테스트 4 〉	통과 (0.03ms, 73.3MB)
    테스트 5 〉	통과 (0.06ms, 77.7MB)
    테스트 6 〉	통과 (0.02ms, 73.6MB)
    테스트 7 〉	통과 (0.04ms, 81.9MB)
 */