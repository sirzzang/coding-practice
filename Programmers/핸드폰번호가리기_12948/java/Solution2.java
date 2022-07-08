package Programmers.핸드폰번호가리기_12948.java;

public class Solution2 {
    public String solution(String phone_number) {
        int phoneNumLength = phone_number.length();
        return "*".repeat(phoneNumLength-4) + 
            phone_number.substring(phoneNumLength-4, phoneNumLength);
    }
}

/**
 * 정확성  테스트
    테스트 1 〉	통과 (1.25ms, 76.5MB)
    테스트 2 〉	통과 (1.16ms, 75.2MB)
    테스트 3 〉	통과 (1.13ms, 77.6MB)
    테스트 4 〉	통과 (1.26ms, 82.8MB)
    테스트 5 〉	통과 (1.15ms, 72.3MB)
    테스트 6 〉	통과 (1.31ms, 81.9MB)
    테스트 7 〉	통과 (1.18ms, 74.9MB)
    테스트 8 〉	통과 (1.17ms, 77.2MB)
    테스트 9 〉	통과 (1.12ms, 80.6MB)
    테스트 10 〉	통과 (1.20ms, 77MB)
    테스트 11 〉	통과 (1.10ms, 73.4MB)
    테스트 12 〉	통과 (1.32ms, 78MB)
    테스트 13 〉	통과 (1.17ms, 77.2MB)
 */