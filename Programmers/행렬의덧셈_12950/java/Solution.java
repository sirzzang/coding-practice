package Programmers.행렬의덧셈_12950.java;

public class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int row = arr1.length;
        int col = arr1[row-1].length;
        int[][] answer = new int[row][col];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                answer[i][j] = arr1[i][j] + arr2[i][j];
            }
        }
        
        return answer;
    }
}

/**
 * 정확성  테스트
    테스트 1 〉	통과 (0.02ms, 75.6MB)
    테스트 2 〉	통과 (0.04ms, 75MB)
    테스트 3 〉	통과 (0.08ms, 73.3MB)
    테스트 4 〉	통과 (0.06ms, 76.9MB)
    테스트 5 〉	통과 (0.04ms, 79.5MB)
    테스트 6 〉	통과 (0.05ms, 78MB)
    테스트 7 〉	통과 (0.01ms, 74.8MB)
    테스트 8 〉	통과 (0.06ms, 76.5MB)
    테스트 9 〉	통과 (0.26ms, 76.5MB)
    테스트 10 〉	통과 (0.20ms, 80.9MB)
    테스트 11 〉	통과 (0.16ms, 80MB)
    테스트 12 〉	통과 (0.27ms, 80.6MB)
    테스트 13 〉	통과 (0.19ms, 78.6MB)
    테스트 14 〉	통과 (0.17ms, 81.4MB)
    테스트 15 〉	통과 (0.20ms, 79.9MB)
    테스트 16 〉	통과 (0.18ms, 79.5MB)
    테스트 17 〉	통과 (3.77ms, 127MB)
 */