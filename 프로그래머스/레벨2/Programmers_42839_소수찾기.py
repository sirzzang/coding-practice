# 시간 효율성 개선 필요
# max vs. sort는 별 차이 없었음.
'''
정확성  테스트
테스트 1 〉	통과 (0.47ms, 10.4MB)
테스트 2 〉	통과 (80.32ms, 15.1MB)
테스트 3 〉	통과 (0.04ms, 10.4MB)
테스트 4 〉	통과 (29.44ms, 12.5MB)
테스트 5 〉	통과 (400.63ms, 35.6MB)
테스트 6 〉	통과 (0.04ms, 10.4MB)
테스트 7 〉	통과 (0.51ms, 10.4MB)
테스트 8 〉	통과 (832.02ms, 52.4MB)
테스트 9 〉	통과 (0.08ms, 10.4MB)
테스트 10 〉	통과 (111.04ms, 17.7MB)
테스트 11 〉	통과 (9.42ms, 10.7MB)
테스트 12 〉	통과 (4.91ms, 10.5MB)
'''
from itertools import permutations  

def get_possible_cases(num_list):
    cases = []
    for i in range(1, len(num_list)+1):
        for perm in permutations(num_list, i):
            temp = int(''.join(map(str, perm)))
            if temp and temp not in cases: # 0 제외
                cases.append(temp)
    cases.sort() # 정렬: max랑 시간복잡도 비교
    return cases

def get_prime_numbers(n):
    prime_list = [True]*(n+1) # 1도 소수로 간주하고 시작
    for i in range(2, int(n**0.5)+2):
        if prime_list[i]:
            for j in range(i+i, n+1, i):
                prime_list[j] = False
    return prime_list

def solution(numbers):
    answer = 0
    cases = get_possible_cases(numbers)
    prime_numbers = get_prime_numbers(cases[-1])
    for case in cases:
        if case == 1: # 1은 소수 아니므로 제외
            continue
        answer += prime_numbers[case]
    
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.50ms, 10.5MB)
테스트 2 〉	통과 (80.45ms, 15.2MB)
테스트 3 〉	통과 (0.04ms, 10.4MB)
테스트 4 〉	통과 (27.37ms, 12.6MB)
테스트 5 〉	통과 (450.44ms, 35.4MB)
테스트 6 〉	통과 (0.04ms, 10.2MB)
테스트 7 〉	통과 (0.51ms, 10.4MB)
테스트 8 〉	통과 (866.83ms, 52.5MB)
테스트 9 〉	통과 (1.14ms, 10.3MB)
테스트 10 〉	통과 (102.30ms, 17.7MB)
테스트 11 〉	통과 (9.47ms, 10.8MB)
테스트 12 〉	통과 (4.99ms, 10.5MB)
'''
from itertools import permutations  

def get_possible_cases(num_list):
    cases = []
    for i in range(1, len(num_list)+1):
        for perm in permutations(num_list, i):
            temp = int(''.join(map(str, perm)))
            if temp and temp not in cases: # 0 제외
                cases.append(temp)
    return cases

def get_prime_numbers(n):
    prime_list = [True]*(n+1) # 1도 소수로 간주하고 시작
    for i in range(2, int(n**0.5)+2):
        if prime_list[i]:
            for j in range(i+i, n+1, i):
                prime_list[j] = False
    return prime_list

def solution(numbers):
    answer = 0
    cases = get_possible_cases(numbers)
    prime_numbers = get_prime_numbers(max(cases)) # 정렬 대신 max
    for case in cases:
        if case == 1: # 1은 소수 아니므로 제외
            continue
        answer += prime_numbers[case]
    
    return answer