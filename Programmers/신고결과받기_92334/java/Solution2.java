package Programmers.신고결과받기_92334;

import java.util.*;

public class Solution2 {
    public int[] solution(String[] id_list, String[] report, int k) {
        
        // 유저 수
        int userNum = id_list.length;
        
        // 유저별 id index
        Map<String, Integer> userIndex = new HashMap<>();
        for (int i = 0; i < userNum; i++) {
            userIndex.put(id_list[i], i);
        }
        
        // 중복 신고 제거
        LinkedHashSet<String> reportSet = new LinkedHashSet<>(Arrays.asList(report));
        String[] reportArr = reportSet.toArray(new String[0]);
        
        // 신고자 및 피신고자별 신고 횟수 집계
        int[][] reportTable = new int[userNum][userNum];
        for (String r : reportArr) {
            String[] reportInfo = r.split(" ");
            int reporterIndex = userIndex.get(reportInfo[0]);
            int reporteeIndex = userIndex.get(reportInfo[1]);
            reportTable[reporterIndex][reporteeIndex] += 1;
            
        }
        
        // 유저별 피신고 횟수
        Map<Integer, Integer> reportCount = new HashMap<>();
        for (int col = 0; col < userNum; col++) {
            
            int colSum = 0;
            for (int row = 0; row < userNum; row++) {
                colSum += reportTable[row][col];
            }
            reportCount.put(col, colSum);
        }
        
        // 유저별 신고 처리 횟수
        int[] answer = new int[userNum];
        for (int row = 0; row < userNum; row++) {
            for (int col = 0; col < userNum; col++) {
                if (reportCount.get(col) < k) continue;
                answer[row] += reportTable[row][col];
            }
        }
        
        return answer;
    }
}

/**
 * 정확성  테스트
    테스트 1 〉	통과 (0.29ms, 73.8MB)
    테스트 2 〉	통과 (0.51ms, 71.8MB)
    테스트 3 〉	통과 (154.28ms, 185MB)
    테스트 4 〉	통과 (0.61ms, 80.6MB)
    테스트 5 〉	통과 (0.44ms, 74.5MB)
    테스트 6 〉	통과 (3.89ms, 84.5MB)
    테스트 7 〉	통과 (5.59ms, 84.5MB)
    테스트 8 〉	통과 (7.24ms, 94.3MB)
    테스트 9 〉	통과 (91.92ms, 148MB)
    테스트 10 〉	통과 (83.22ms, 138MB)
    테스트 11 〉	통과 (163.15ms, 177MB)
    테스트 12 〉	통과 (6.38ms, 82.9MB)
    테스트 13 〉	통과 (6.35ms, 80.8MB)
    테스트 14 〉	통과 (102.84ms, 153MB)
    테스트 15 〉	통과 (126.29ms, 161MB)
    테스트 16 〉	통과 (1.57ms, 79.2MB)
    테스트 17 〉	통과 (5.14ms, 77.9MB)
    테스트 18 〉	통과 (7.15ms, 80.9MB)
    테스트 19 〉	통과 (7.80ms, 82.2MB)
    테스트 20 〉	통과 (96.81ms, 137MB)
    테스트 21 〉	통과 (136.60ms, 161MB)
    테스트 22 〉	통과 (0.23ms, 73.3MB)
    테스트 23 〉	통과 (0.23ms, 71.5MB)
    테스트 24 〉	통과 (0.25ms, 79.3MB)
 */