package Programmers.하샤드수_12947.java;

class Solution {
    public boolean solution(int x) {
        
        int sum = 0;
        
        // 자연수 자리 합
        String xStr = Integer.toString(x);
        for (int i = 0; i < xStr.length(); i++) {
            sum += Integer.parseInt(String.valueOf(xStr.charAt(i)));
        }
        
        // 합이 0인 경우
//         if (sum == 0) {
//             return false;
//         }
        
        return x % sum == 0;
    }
}

/**
 * 정확성  테스트
    테스트 1 〉	통과 (0.03ms, 76MB)
    테스트 2 〉	통과 (0.04ms, 72.8MB)
    테스트 3 〉	통과 (0.04ms, 77.7MB)
    테스트 4 〉	통과 (0.04ms, 85.9MB)
    테스트 5 〉	통과 (0.03ms, 75.7MB)
    테스트 6 〉	통과 (0.03ms, 73.2MB)
    테스트 7 〉	통과 (0.03ms, 73.7MB)
    테스트 8 〉	통과 (0.03ms, 78.7MB)
    테스트 9 〉	통과 (0.03ms, 70.4MB)
    테스트 10 〉	통과 (0.03ms, 68.4MB)
    테스트 11 〉	통과 (0.04ms, 76MB)
    테스트 12 〉	통과 (0.04ms, 72.7MB)
    테스트 13 〉	통과 (0.03ms, 74.8MB)
    테스트 14 〉	통과 (0.03ms, 73.7MB)
    테스트 15 〉	통과 (0.04ms, 76.4MB)
    테스트 16 〉	통과 (0.03ms, 72.7MB)
    테스트 17 〉	통과 (0.04ms, 68.1MB)
 */