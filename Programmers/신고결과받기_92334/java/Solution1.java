package Programmers.신고결과받기_92334;

import java.util.*;

class Solution1 {
    public int[] solution(String[] id_list, String[] report, int k) {
        
        // 유저 수
        int userNum = id_list.length;
        
        // 유저별 id index
        Map<String, Integer> userIndex = new HashMap<>();
        for (int i = 0; i < userNum; i++) {
            userIndex.put(id_list[i], i);
        }
        
        // 신고자 및 피신고자별 신고 횟수 집계
        int[][] reportTable = new int[userNum][userNum];
        for (String r : report) {
            String[] reportInfo = r.split(" ");
            int reporterIndex = userIndex.get(reportInfo[0]);
            int reporteeIndex = userIndex.get(reportInfo[1]);
                        
            // 신고자와 피신고자가 동일한 경우(중복 신고) 집계 제외
            if (reportTable[reporterIndex][reporteeIndex] >= 1) continue;
            
            // System.out.println(reportInfo[0] + " reported " + reportInfo[1]);
            reportTable[reporterIndex][reporteeIndex] += 1;
            
        }
        
        // System.out.println(Arrays.deepToString(reportTable));
        
        
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
    테스트 1 〉	통과 (0.17ms, 72.4MB)
    테스트 2 〉	통과 (0.18ms, 72MB)
    테스트 3 〉	통과 (122.29ms, 175MB)
    테스트 4 〉	통과 (0.29ms, 76MB)
    테스트 5 〉	통과 (0.30ms, 86MB)
    테스트 6 〉	통과 (3.36ms, 80MB)
    테스트 7 〉	통과 (5.35ms, 82.7MB)
    테스트 8 〉	통과 (8.84ms, 82.2MB)
    테스트 9 〉	통과 (61.46ms, 125MB)
    테스트 10 〉	통과 (63.10ms, 152MB)
    테스트 11 〉	통과 (118.76ms, 161MB)
    테스트 12 〉	통과 (5.73ms, 76.4MB)
    테스트 13 〉	통과 (5.12ms, 67.4MB)
    테스트 14 〉	통과 (73.61ms, 132MB)
    테스트 15 〉	통과 (105.10ms, 158MB)
    테스트 16 〉	통과 (1.22ms, 75.7MB)
    테스트 17 〉	통과 (4.55ms, 80.8MB)
    테스트 18 〉	통과 (6.18ms, 77.7MB)
    테스트 19 〉	통과 (7.19ms, 78.4MB)
    테스트 20 〉	통과 (74.60ms, 143MB)
    테스트 21 〉	통과 (118.23ms, 160MB)
    테스트 22 〉	통과 (0.07ms, 77.6MB)
    테스트 23 〉	통과 (0.08ms, 70.5MB)
    테스트 24 〉	통과 (0.14ms, 77.6MB)
 */