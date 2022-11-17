package Programmers.햄버거만들기_133502.java;

import java.util.*;

public class Solution1 {

    public int solution(int[] ingredient) {
        int answer = 0;
        List<Integer> burger = new ArrayList<>(Arrays.asList(1, 2, 3, 1));

        Stack<Integer> stack = new Stack<>();
        for (int i : ingredient) {
            stack.push(i); // auto boxing

            if (stack.size() >= 4 &&
                stack.subList(stack.size()-4, stack.size()).equals(burger)
               ) {
                answer++;
                for (int j=0; j<4; j++) {
                    stack.pop();
                }
            }
        }
        return answer;
    }
}

/**
 * 정확성  테스트
테스트 1 〉	통과 (0.90ms, 71.5MB)
테스트 2 〉	통과 (2.47ms, 70.4MB)
테스트 3 〉	통과 (248.68ms, 130MB)
테스트 4 〉	통과 (230.69ms, 145MB)
테스트 5 〉	통과 (225.14ms, 163MB)
테스트 6 〉	통과 (135.31ms, 122MB)
테스트 7 〉	통과 (242.45ms, 152MB)
테스트 8 〉	통과 (148.21ms, 138MB)
테스트 9 〉	통과 (228.29ms, 135MB)
테스트 10 〉	통과 (19.03ms, 68.3MB)
테스트 11 〉	통과 (132.06ms, 107MB)
테스트 12 〉	통과 (161.48ms, 182MB)
테스트 13 〉	통과 (0.21ms, 83.9MB)
테스트 14 〉	통과 (0.83ms, 72.6MB)
테스트 15 〉	통과 (0.86ms, 85.8MB)
테스트 16 〉	통과 (0.21ms, 66.6MB)
테스트 17 〉	통과 (0.15ms, 78.1MB)
테스트 18 〉	통과 (0.66ms, 80MB)
 */

