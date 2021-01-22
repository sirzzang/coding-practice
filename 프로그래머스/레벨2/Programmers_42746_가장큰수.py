# 풀이 1) 시간 초과: 버블 정렬 방식 응용
'''
정확성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	통과 (3171.42ms, 10.4MB)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	실패 (시간 초과)
테스트 7 〉	통과 (0.44ms, 10.3MB)
테스트 8 〉	통과 (0.18ms, 10.4MB)
테스트 9 〉	통과 (0.24ms, 10.3MB)
테스트 10 〉	통과 (0.21ms, 10.3MB)
테스트 11 〉	통과 (0.00ms, 10.1MB)
'''

from functools import cmp_to_key


def solution(numbers):
    if sum(numbers) == 0:
        return '0'

    for i in range(len(numbers)):
        for j in range(len(numbers)-1):
            prev_, next_ = str(numbers[j]), str(numbers[j+1])
            if int(prev_ + next_) < int(next_ + prev_):
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]  # swap

    answer = ''
    for n in numbers:
        answer += str(n)
    return answer


# 풀이 2) compare key 이용: 앞의 것이 크면 1, 뒤의 것이 크면 -1 반환하는 정렬 기준.
'''
정확성  테스트
테스트 1 〉	통과 (415.90ms, 21.7MB)
테스트 2 〉	통과 (212.00ms, 16.5MB)
테스트 3 〉	통과 (538.67ms, 25.3MB)
테스트 4 〉	통과 (8.47ms, 10.6MB)
테스트 5 〉	통과 (346.54ms, 20.3MB)
테스트 6 〉	통과 (289.88ms, 19MB)
테스트 7 〉	통과 (0.09ms, 10.4MB)
테스트 8 〉	통과 (0.05ms, 10.4MB)
테스트 9 〉	통과 (0.07ms, 10.4MB)
테스트 10 〉	통과 (0.05ms, 10.4MB)
테스트 11 〉	통과 (0.00ms, 10.1MB)
'''


def compare(x, y):
    return int(x+y) - int(y+x)


def solution(numbers):
    if sum(numbers) == 0:
        return '0'

    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=cmp_to_key(compare), reverse=True)
    return ''.join(numbers)


# 풀이 3) 주어진 수를 반복하여 4자리 수를 만들어 큰 순서대로 정렬
'''
정확성  테스트
테스트 1 〉	통과 (52.54ms, 23.3MB)
테스트 2 〉	통과 (25.91ms, 17.1MB)
테스트 3 〉	통과 (70.24ms, 27.4MB)
테스트 4 〉	통과 (1.78ms, 10.4MB)
테스트 5 〉	통과 (43.21ms, 21.8MB)
테스트 6 〉	통과 (36.71ms, 20.3MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.1MB)
테스트 10 〉	통과 (0.02ms, 10.2MB)
테스트 11 〉	통과 (0.00ms, 10.2MB)
'''


def solution(numbers):
    if sum(numbers) == 0:
        return '0'

    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: str(x*4)[:4], reverse=True)
    return ''.join(numbers)
