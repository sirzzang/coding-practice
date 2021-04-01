# 문제 설명에 충실한 시간초과 풀이(...)
'''
정확성  테스트
테스트 1 〉	통과 (0.17ms, 10.3MB)
테스트 2 〉	통과 (0.16ms, 10.3MB)
테스트 3 〉	통과 (1.39ms, 10.4MB)
테스트 4 〉	통과 (8.66ms, 10.6MB)
테스트 5 〉	통과 (38.39ms, 10.6MB)
테스트 6 〉	통과 (90.42ms, 10.5MB)
테스트 7 〉	통과 (39.27ms, 10.9MB)
테스트 8 〉	통과 (177.97ms, 12.7MB)
테스트 9 〉	통과 (191.95ms, 12.9MB)
테스트 10 〉	통과 (202.61ms, 12.8MB)
테스트 11 〉	통과 (38.38ms, 10.7MB)
테스트 12 〉	통과 (88.52ms, 10.6MB)
테스트 13 〉	통과 (36.86ms, 11.1MB)
테스트 14 〉	통과 (189.46ms, 11.6MB)
테스트 15 〉	통과 (187.04ms, 11.7MB)
테스트 16 〉	통과 (38.23ms, 10.7MB)
테스트 17 〉	통과 (88.68ms, 10.7MB)
테스트 18 〉	통과 (184.89ms, 11.6MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
'''


def solution(info, query):
    answer = []
    info = [i.split() for i in info]
    query = [[elem for elem in q.split() if not elem == 'and'] for q in query]

    for q in query:
        cnt = 0
        for candidate in info:
            for i in range(4):
                if q[i] == '-':
                    continue
                if q[i] != candidate[i]:
                    break
            else:
                if int(candidate[4]) >= int(q[4]):
                    cnt += 1

        answer.append(cnt)

    return answer
