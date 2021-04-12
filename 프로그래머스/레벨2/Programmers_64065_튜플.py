'''
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.4MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (0.06ms, 10.3MB)
테스트 5 〉	통과 (0.25ms, 10.4MB)
테스트 6 〉	통과 (1.07ms, 10.5MB)
테스트 7 〉	통과 (4.74ms, 11.8MB)
테스트 8 〉	통과 (13.36ms, 14.9MB)
테스트 9 〉	통과 (6.36ms, 12.4MB)
테스트 10 〉	통과 (14.51ms, 15.6MB)
테스트 11 〉	통과 (18.19ms, 17MB)
테스트 12 〉	통과 (24.32ms, 20.1MB)
테스트 13 〉	통과 (26.02ms, 20.1MB)
테스트 14 〉	통과 (26.60ms, 20.5MB)
테스트 15 〉	통과 (0.03ms, 10.3MB)
'''


def nested_frequency(items):
    frequency = {}
    for item in items:
        for i in item:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
    return frequency


def solution(s):
    tuples = [_s.lstrip('{').rstrip('}') for _s in s.split('},')]
    tuples.sort(key=lambda x: len(x), reverese=True)
    freq = nested_frequency(tuples)
    tuples[0].sort(key=lambda x: freq[x], reverse=True)
    answer = list(map(int, tuples[0]))

    return answer
