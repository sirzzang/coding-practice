package Programmers.푸드파이트대회_134240.java;

class Solutin1 {

    public static String solution(int[] food) {

        String forward = "";
        String backward = "";
        
        for (int i = 1; i < food.length; i++) {
            String num = Integer.toString(i);
            int count = food[i] / 2;
            forward += num.repeat(count);
            backward = num.repeat(count) + backward;
        }
                
        return forward + "0" + backward;
    }

    public static void main(String[] args) {
        System.out.println(solution(new int[]{1, 3, 4, 6}));
        System.out.println(solution(new int[]{1, 7, 1, 2}));
    }
}

/**
 * 정확성  테스트
테스트 1 〉	통과 (11.05ms, 78.6MB)
테스트 2 〉	통과 (12.65ms, 89.1MB)
테스트 3 〉	통과 (12.78ms, 74.9MB)
테스트 4 〉	통과 (8.32ms, 71.8MB)
테스트 5 〉	통과 (10.24ms, 74.1MB)
테스트 6 〉	통과 (13.39ms, 77.3MB)
테스트 7 〉	통과 (12.89ms, 78.6MB)
테스트 8 〉	통과 (10.14ms, 75.7MB)
테스트 9 〉	통과 (8.67ms, 81MB)
테스트 10 〉	통과 (11.15ms, 75.3MB)
테스트 11 〉	통과 (11.12ms, 85.8MB)
테스트 12 〉	통과 (10.51ms, 75.3MB)
테스트 13 〉	통과 (10.34ms, 76.2MB)
테스트 14 〉	통과 (8.88ms, 79.4MB)
테스트 15 〉	통과 (11.41ms, 74MB)
테스트 16 〉	통과 (12.72ms, 74.3MB)
테스트 17 〉	통과 (10.49ms, 82.9MB)
테스트 18 〉	통과 (14.90ms, 78.6MB)
테스트 19 〉	통과 (11.47ms, 82.3MB)
테스트 20 〉	통과 (16.92ms, 75.5MB)
 */