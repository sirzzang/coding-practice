package Programmers.직사각형별찍기_12969.java;

import java.util.Scanner;

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        
        String stars = "*".repeat(a);
        for (int i = 0; i < b; i++) {
            System.out.println(stars);
        }
    }
}

/**
 * 정확성  테스트
    테스트 1 〉	통과 (135.75ms, 65.5MB)
    테스트 2 〉	통과 (148.34ms, 74.1MB)
    테스트 3 〉	통과 (127.31ms, 64.3MB)
    테스트 4 〉	통과 (147.97ms, 66.5MB)
    테스트 5 〉	통과 (129.37ms, 68.5MB)
    테스트 6 〉	통과 (126.94ms, 67MB)
    테스트 7 〉	통과 (131.59ms, 74.7MB)
    테스트 8 〉	통과 (135.22ms, 69.2MB)
    테스트 9 〉	통과 (149.34ms, 64.8MB)
    테스트 10 〉	통과 (135.48ms, 68.3MB)
    테스트 11 〉	통과 (132.24ms, 69.7MB)
 */