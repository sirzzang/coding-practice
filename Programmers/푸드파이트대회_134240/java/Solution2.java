package Programmers.푸드파이트대회_134240.java;

public class Solution2 {

    public String solution(int[] food) {
        StringBuffer sbForward = new StringBuffer();
        StringBuffer sbBackward = new StringBuffer();
        
        for (int i = 1; i < food.length; i++) {
            String num = String.valueOf(i);
            int count = food[i]/2;
            sbForward.append(num.repeat(count));
            sbBackward.insert(0, num.repeat(count));
        }
                    
        return sbForward.append(0).append(sbBackward).toString();
    }
    
}

/**
 * 정확성  테스트
테스트 1 〉	통과 (0.15ms, 80.9MB)
테스트 2 〉	통과 (0.16ms, 76.5MB)
테스트 3 〉	통과 (0.17ms, 70.4MB)
테스트 4 〉	통과 (0.28ms, 73.6MB)
테스트 5 〉	통과 (0.15ms, 70.1MB)
테스트 6 〉	통과 (0.32ms, 85.8MB)
테스트 7 〉	통과 (0.23ms, 72MB)
테스트 8 〉	통과 (0.14ms, 73.6MB)
테스트 9 〉	통과 (0.13ms, 77.2MB)
테스트 10 〉	통과 (0.14ms, 73.6MB)
테스트 11 〉	통과 (0.10ms, 70MB)
테스트 12 〉	통과 (0.20ms, 72.7MB)
테스트 13 〉	통과 (0.10ms, 73.1MB)
테스트 14 〉	통과 (0.37ms, 74.1MB)
테스트 15 〉	통과 (0.10ms, 75.7MB)
테스트 16 〉	통과 (0.17ms, 72.8MB)
테스트 17 〉	통과 (0.12ms, 76.5MB)
테스트 18 〉	통과 (0.15ms, 72.4MB)
테스트 19 〉	통과 (0.14ms, 73.3MB)
테스트 20 〉	통과 (0.13ms, 86.8MB)
 */