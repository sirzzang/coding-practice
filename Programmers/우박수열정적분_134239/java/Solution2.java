package Programmers.우박수열정적분_134239.java;

public class Solution2 {
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
            System.out.println(start + ", " + end);
            if (start == end) {
                answer[i] = 0;
            } else if (start > end) {
                answer[i] = -1;
            } else {
                double sum = 0;
                
                // TODO
                answer[i] = integral.stream()
                    .skip(start)
                    .limit(end) // Stream<Double>
                    .reduce(0.0, Double::sum);
                    // .mapToDouble(n -> n) // DoubleStream
                    // .sum();
            }
        }
        
        return answer;
}