package Programmers.푸드파이트대회_134240.java;

public class Solution3 {
    public String solution(int[] food) {
        
        StringBuffer sb = new StringBuffer();
        
        for (int i = 1; i < food.length; i++) {
            String num = String.valueOf(i);
            int count = food[i]/2;
            sb.append(num.repeat(count));
        }
        
        String answer = sb.toString() + "0";
                    
        return answer + sb.reverse();
    }
}

/**
 * 정확성  테스트
테스트 1 〉	통과 (2.99ms, 77.7MB)
테스트 2 〉	통과 (2.20ms, 74.7MB)
테스트 3 〉	통과 (2.83ms, 72.9MB)
테스트 4 〉	통과 (2.54ms, 72.9MB)
테스트 5 〉	통과 (2.79ms, 81.7MB)
테스트 6 〉	통과 (2.31ms, 77.4MB)
테스트 7 〉	통과 (2.76ms, 73.8MB)
테스트 8 〉	통과 (2.84ms, 79.7MB)
테스트 9 〉	통과 (2.95ms, 73.4MB)
테스트 10 〉	통과 (2.22ms, 75.6MB)
테스트 11 〉	통과 (3.08ms, 79.2MB)
테스트 12 〉	통과 (3.32ms, 70MB)
테스트 13 〉	통과 (2.24ms, 72.1MB)
테스트 14 〉	통과 (3.89ms, 81.5MB)
테스트 15 〉	통과 (2.25ms, 74.2MB)
테스트 16 〉	통과 (2.27ms, 76.2MB)
테스트 17 〉	통과 (2.64ms, 77.8MB)
테스트 18 〉	통과 (2.33ms, 74.7MB)
테스트 19 〉	통과 (2.85ms, 72.5MB)
테스트 20 〉	통과 (3.81ms, 83.9MB)
 */
