package Programmers.햄버거만들기_133502;

// https://school.programmers.co.kr/learn/courses/30/lessons/133502/solution_groups?language=java
public class Solution {
    public int solution(int[] ingredient) {
        int[] stack = new int[ingredient.length]; // stack을 굳이 collection 자료구조 사용할 필요 없음
        int sp = 0; // 비교 시 stack pointer를 이용하면 됨
        int answer = 0;
        for (int i : ingredient) {
            stack[sp++] = i;
            // 길이 및 햄버거 비교 로직 구현 시, size, length 등 이용하는 것보다 stack pointer 이용할 떄 더 간결
            if (sp >= 4 && stack[sp - 1] == 1 
                && stack[sp - 2] == 3
                && stack[sp - 3] == 2
                && stack[sp - 4] == 1) {
                sp -= 4; // 햄버거 만들어지면 포인터 앞으로 옮기면 삭제한 효과가 남
                answer++;
            }
        }
        return answer;
    }
}
