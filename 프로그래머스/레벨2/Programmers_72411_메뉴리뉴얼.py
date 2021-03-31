'''
정확성  테스트
테스트 1 〉	통과 (0.13ms, 10.3MB)
테스트 2 〉	통과 (0.07ms, 10.2MB)
테스트 3 〉	통과 (0.17ms, 10MB)
테스트 4 〉	통과 (0.17ms, 10.2MB)
테스트 5 〉	통과 (0.14ms, 10.2MB)
테스트 6 〉	통과 (0.52ms, 10.3MB)
테스트 7 〉	통과 (0.58ms, 10.2MB)
테스트 8 〉	통과 (9.11ms, 10.3MB)
테스트 9 〉	통과 (7.14ms, 10.2MB)
테스트 10 〉	통과 (4.68ms, 10.3MB)
테스트 11 〉	통과 (2.66ms, 10.1MB)
테스트 12 〉	통과 (2.39ms, 10.3MB)
테스트 13 〉	통과 (4.65ms, 10.4MB)
테스트 14 〉	통과 (1.67ms, 10.4MB)
테스트 15 〉	통과 (4.54ms, 10.4MB)
테스트 16 〉	통과 (2.28ms, 10.2MB)
테스트 17 〉	통과 (0.50ms, 10.2MB)
테스트 18 〉	통과 (0.16ms, 10.2MB)
테스트 19 〉	통과 (0.03ms, 10.2MB)
테스트 20 〉	통과 (1.45ms, 10.2MB)
'''

# 이게 왜 되지?
from itertools import combinations

def solution(orders, course):
    answer = []

    for c in course:
        temp = {} # 가능한 메뉴 조합을 담을 임시 배열
        for order in orders:
            for menu in combinations(order, c):
                menu = ''.join(sorted(menu)) # 손님들이 주문한 메뉴에서 가능한 코스 조합
                if menu in temp:
                    temp[menu] += 1
                else:
                    temp[menu] = 1

        # 2명 이상에게, 가장 많이 주문된 매뉴 배열만 찾기
        temp = {k:v for k, v in temp.items() if v >= 2 and v == max(temp.values())}
        if temp:
            answer.extend([k for k in temp.keys()])

    answer.sort() # 알파벳 순 정렬

    return answer
