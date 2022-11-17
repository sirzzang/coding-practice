package Programmers.우박수열정적분_134239.java;

import java.util.ArrayList;

public class Solution1 {

    public double[] solution(int k, int[][] ranges) {
        double[] answer = new double[ranges.length];
        
        // 우박 수열 구간별 정적분값 구하기
        ArrayList<Double> integral = new ArrayList<>();
        while (k != 1) {
            double prev = k;
            if (k % 2 == 0) {
                k /= 2;
            } else {
                k = 3 * k + 1;
            }
            integral.add((prev + k) / 2); // type conversion
        }
        
        // 구간별 정적분 값 구하기
        for (int i=0; i<ranges.length; i++) {
            int start = ranges[i][0];
            int end = integral.size() + ranges[i][1];
            if (start == end) {
                answer[i] = 0;
            } else if (start > end) {
                answer[i] = -1;
            } else {
                double sum = 0;
                for (int j = start; j < end; j++) {
                    sum += integral.get(j);
                }
                answer[i] = sum;
            }
        }
        
        return answer;
    }
    
}


/**
 * 정확성  테스트
테스트 1 〉	통과 (0.03ms, 76.5MB)
테스트 2 〉	통과 (0.60ms, 75.5MB)
테스트 3 〉	통과 (11.71ms, 95.3MB)
테스트 4 〉	통과 (1.90ms, 84.7MB)
테스트 5 〉	통과 (0.54ms, 83.7MB)
테스트 6 〉	통과 (4.13ms, 79.6MB)
테스트 7 〉	통과 (13.18ms, 103MB)
테스트 8 〉	통과 (10.44ms, 91.5MB)
테스트 9 〉	통과 (0.27ms, 77.5MB)
테스트 10 〉	통과 (7.12ms, 81.6MB)
 */