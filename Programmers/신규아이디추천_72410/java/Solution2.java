package Programmers.신규아이디추천_72410.java;

public class Solution2 {

    public String solution(String new_id) {
        
        String answer;
        
        answer = new_id
            .toLowerCase()
            .replaceAll("[^a-z0-9\\-\\_\\.]", "") // 2단계
            .replaceAll("\\.{2,}", ".") // 3단계
            .replaceAll("^[.]+|[.]+$", ""); // 4단계
        
        if (answer.length() == 0) {
            answer = "a";
        } // 5단계

        if (answer.length() >= 16) {
            answer = answer.substring(0, 15)
                .replaceAll("\\.$", "");
        } // 6단계

        int len = answer.length();
        if (len <= 2) {
            String lastChar = answer.substring(len - 1);
            answer += lastChar.repeat(3 - len);
        } // 7단계

        return answer;
    }

}

/**
 * 정확성  테스트
    테스트 1 〉	통과 (0.17ms, 74MB)
    테스트 2 〉	통과 (1.19ms, 68.5MB)
    테스트 3 〉	통과 (1.34ms, 77.6MB)
    테스트 4 〉	통과 (0.21ms, 74.4MB)
    테스트 5 〉	통과 (0.24ms, 87.4MB)
    테스트 6 〉	통과 (0.17ms, 76.9MB)
    테스트 7 〉	통과 (0.19ms, 79.9MB)
    테스트 8 〉	통과 (0.26ms, 77.3MB)
    테스트 9 〉	통과 (1.26ms, 73.8MB)
    테스트 10 〉	통과 (0.16ms, 75.4MB)
    테스트 11 〉	통과 (0.22ms, 79.4MB)
    테스트 12 〉	통과 (0.36ms, 72.3MB)
    테스트 13 〉	통과 (1.37ms, 77.3MB)
    테스트 14 〉	통과 (0.25ms, 72MB)
    테스트 15 〉	통과 (0.30ms, 74.5MB)
    테스트 16 〉	통과 (0.51ms, 78MB)
    테스트 17 〉	통과 (1.18ms, 76.5MB)
    테스트 18 〉	통과 (1.50ms, 73.7MB)
    테스트 19 〉	통과 (2.12ms, 77.3MB)
    테스트 20 〉	통과 (2.62ms, 75.8MB)
    테스트 21 〉	통과 (2.24ms, 79.5MB)
    테스트 22 〉	통과 (3.72ms, 77.1MB)
    테스트 23 〉	통과 (2.19ms, 75.6MB)
    테스트 24 〉	통과 (1.75ms, 73.3MB)
    테스트 25 〉	통과 (1.37ms, 76.7MB)
    테스트 26 〉	통과 (1.15ms, 72.2MB)
 */