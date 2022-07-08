package Programmers.핸드폰번호가리기_12948.java;

public class Solution1 {
    public String solution(String phone_number) {
        String answer = "";
        int phoneNumLength = phone_number.length();
        for (int i=0; i < phoneNumLength ; i++) {
            if (i < phoneNumLength - 4) {
                answer += "*";
            } else {
                answer += phone_number.charAt(i);
            }
        }
        return answer;
    }
}

/**
 * 정확성  테스트
    테스트 1 〉	통과 (9.39ms, 79.4MB)
    테스트 2 〉	통과 (9.53ms, 79.5MB)
    테스트 3 〉	통과 (9.93ms, 77.5MB)
    테스트 4 〉	통과 (9.88ms, 85.2MB)
    테스트 5 〉	통과 (10.45ms, 79.1MB)
    테스트 6 〉	통과 (9.03ms, 76.6MB)
    테스트 7 〉	통과 (9.55ms, 75.9MB)
    테스트 8 〉	통과 (9.74ms, 76.9MB)
    테스트 9 〉	통과 (8.98ms, 80.3MB)
    테스트 10 〉	통과 (9.41ms, 70.1MB)
    테스트 11 〉	통과 (8.79ms, 73.2MB)
    테스트 12 〉	통과 (9.02ms, 76.9MB)
    테스트 13 〉	통과 (9.61ms, 73.3MB)
 */