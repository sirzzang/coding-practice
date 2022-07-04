package Programmers.신규아이디추천_72410.java;

public class Solution3 {

    public String solution(String new_id) {
        SolutionBuilder solutionBuilder = new SolutionBuilder(new_id)
            .toLower() // 1단계
            .replaceChars() // 2단계
            .deleteDoubleDots() // 3단계
            .trimDots() // 4단계
            .checkEmpty() // 5단계
            .checkLong() // 6단계
            .padThree(); // 7단계
        
        return solutionBuilder.getId();
    }

    public static class SolutionBuilder {
        private String id;

        public SolutionBuilder(String id) {
            this.id = id;
        }

        public String getId() {
            return id;
        }

        public SolutionBuilder toLower() {
            id = id.toLowerCase();
            return this;
        }

        public SolutionBuilder replaceChars() {
            id = id.replaceAll("[^a-z0-9\\-\\_\\.]", "");
            return this;
        }

        public SolutionBuilder deleteDoubleDots() {
            id = id.replaceAll("\\.{2,}", ".");
            return this;
        }

        public SolutionBuilder trimDots() {
            id = id.replaceAll("^[.]+|[.]+$", "");
            return this;
        }
        
        public SolutionBuilder checkEmpty() {
            id = id.length() == 0 ? "a" : id;
            return this;
        }

        public SolutionBuilder checkLong() {
            id = id.length() >= 16 ? id.substring(0, 15).replaceAll("\\.$", "") : id;
            return this;
        }

        public SolutionBuilder padThree() {
            int len = id.length();
            id = id.length() <= 2 ? 
                id += id.substring(len-1).repeat(3-len) : id;
            return this;
        }
    }
}

/**
 * 정확성  테스트
테스트 1 〉	통과 (0.43ms, 74MB)
테스트 2 〉	통과 (1.61ms, 82.5MB)
테스트 3 〉	통과 (1.55ms, 78.1MB)
테스트 4 〉	통과 (0.40ms, 76.7MB)
테스트 5 〉	통과 (0.40ms, 76.2MB)
테스트 6 〉	통과 (0.40ms, 78.3MB)
테스트 7 〉	통과 (0.37ms, 73.5MB)
테스트 8 〉	통과 (0.40ms, 79MB)
테스트 9 〉	통과 (1.43ms, 75.1MB)
테스트 10 〉	통과 (0.35ms, 82.5MB)
테스트 11 〉	통과 (0.42ms, 76.5MB)
테스트 12 〉	통과 (0.60ms, 77.4MB)
테스트 13 〉	통과 (1.80ms, 75.3MB)
테스트 14 〉	통과 (0.45ms, 76MB)
테스트 15 〉	통과 (0.50ms, 73.4MB)
테스트 16 〉	통과 (0.82ms, 70.8MB)
테스트 17 〉	통과 (1.23ms, 71.6MB)
테스트 18 〉	통과 (1.70ms, 77.1MB)
테스트 19 〉	통과 (2.27ms, 76.5MB)
테스트 20 〉	통과 (2.83ms, 84.4MB)
테스트 21 〉	통과 (2.42ms, 75.8MB)
테스트 22 〉	통과 (3.72ms, 75.6MB)
테스트 23 〉	통과 (2.69ms, 77MB)
테스트 24 〉	통과 (1.75ms, 75.7MB)
테스트 25 〉	통과 (1.75ms, 71.6MB)
테스트 26 〉	통과 (1.42ms, 78.1MB)
 */