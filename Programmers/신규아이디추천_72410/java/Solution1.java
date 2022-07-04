package Programmers.신규아이디추천_72410.java;

public class Solution1 {
    public String solution(String new_id) {
        
        String answer;
        
        answer = new_id
            .toLowerCase() // 1단계
            .replaceAll("[^a-z0-9\\-\\_\\.]", "") // 2단계
            .replaceAll("\\.{2,}", ".") // 3단계
            .replaceAll("^[.]+|[.]+$", ""); // 4단계
        answer = answer.length() == 0 ? "a" : answer; // 5단계
        answer = answer.length() >= 16 ? 
            answer.substring(0, 15).replaceAll("\\.$", "") : answer; // 6단계
        answer = answer.length() <= 2 ? 
            answer += answer.substring(answer.length()-1).repeat(3 - answer.length()) : answer; // 7단계
        
        return answer;
    }
}

/**
 * 정확성  테스트
    테스트 1 〉	통과 (0.27ms, 82.2MB)
    테스트 2 〉	통과 (1.38ms, 75MB)
    테스트 3 〉	통과 (1.72ms, 71.1MB)
    테스트 4 〉	통과 (0.24ms, 77.6MB)
    테스트 5 〉	통과 (0.37ms, 82.6MB)
    테스트 6 〉	통과 (0.17ms, 72.2MB)
    테스트 7 〉	통과 (0.19ms, 70.1MB)
    테스트 8 〉	통과 (0.33ms, 81.2MB)
    테스트 9 〉	통과 (1.34ms, 75MB)
    테스트 10 〉	통과 (0.20ms, 76.5MB)
    테스트 11 〉	통과 (0.20ms, 72.2MB)
    테스트 12 〉	통과 (0.34ms, 71.6MB)
    테스트 13 〉	통과 (1.44ms, 83.8MB)
    테스트 14 〉	통과 (0.25ms, 67.3MB)
    테스트 15 〉	통과 (0.33ms, 73.5MB)
    테스트 16 〉	통과 (0.52ms, 73.1MB)
    테스트 17 〉	통과 (1.05ms, 76.5MB)
    테스트 18 〉	통과 (1.55ms, 75.2MB)
    테스트 19 〉	통과 (1.99ms, 72.7MB)
    테스트 20 〉	통과 (2.60ms, 74.5MB)
    테스트 21 〉	통과 (2.16ms, 73.7MB)
    테스트 22 〉	통과 (4.01ms, 75.5MB)
    테스트 23 〉	통과 (2.30ms, 79MB)
    테스트 24 〉	통과 (1.62ms, 73.5MB)
    테스트 25 〉	통과 (1.38ms, 71.6MB)
    테스트 26 〉	통과 (1.33ms, 74.5MB) 
 */