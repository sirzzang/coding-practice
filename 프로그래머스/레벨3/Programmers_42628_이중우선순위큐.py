'''
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
'''

import heapq


def solution(operations):
    q = []
    for o in operations:
        if o == "D 1":
            if not q:
                continue
            heapq._heapify_max(q)  # 최대힙
            heapq._heappop_max(q)
            # print(heapq._heappop_max(q))
        elif o == "D -1":
            if not q:
                continue
            heapq.heapify(q)  # 최소힙
            heapq.heappop(q)
            # print(heapq.heappop(q))
        else:
            q.append(int(o.split()[-1]))
        # print(o, q)

    if not q:
        return [0, 0]
    return [max(q), min(q)]
