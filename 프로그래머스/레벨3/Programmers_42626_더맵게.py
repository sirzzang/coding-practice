'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.77ms, 10.2MB)
테스트 7 〉	통과 (0.72ms, 10.3MB)
테스트 8 〉	통과 (0.08ms, 10.2MB)
테스트 9 〉	통과 (0.07ms, 10.2MB)
테스트 10 〉	통과 (0.53ms, 10.2MB)
테스트 11 〉	통과 (0.34ms, 10.2MB)
테스트 12 〉	통과 (1.11ms, 10.2MB)
테스트 13 〉	통과 (0.98ms, 10MB)
테스트 14 〉	통과 (0.02ms, 10.2MB)
테스트 15 〉	통과 (0.83ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (179.95ms, 16.3MB)
테스트 2 〉	통과 (403.70ms, 21.9MB)
테스트 3 〉	통과 (1818.67ms, 49.8MB)
테스트 4 〉	통과 (142.43ms, 15MB)
테스트 5 〉	통과 (1908.56ms, 51.8MB)
'''

import heapq


def solution(scoville, K):
    h = scoville
    heapq.heapify(h)
    answer = 0
    while h[0] < K and len(h) >= 2:
        first = heapq.heappop(h)
        second = heapq.heappop(h)
        mix = first + 2 * second
        answer += 1
        heapq.heappush(h, mix)
    print(h)
    if h[0] < K:
        print(-1)
        return -1
    print(answer)
    return answer


if __name__ == '__main__':
    solution([1, 2, 3, 9, 10, 12], 7)
    print('===')
    solution([1, 1, 1], 10)
