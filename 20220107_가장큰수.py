'''
정확성  테스트
테스트 1 〉	통과 (68.05ms, 21.1MB)
테스트 2 〉	통과 (34.48ms, 16.2MB)
테스트 3 〉	통과 (126.79ms, 24.5MB)
테스트 4 〉	통과 (1.78ms, 10.6MB)
테스트 5 〉	통과 (63.53ms, 20MB)
테스트 6 〉	통과 (79.07ms, 18.8MB)
테스트 7 〉	통과 (0.04ms, 10.4MB)
테스트 8 〉	통과 (0.05ms, 10.4MB)
테스트 9 〉	통과 (0.05ms, 10.4MB)
테스트 10 〉	통과 (0.04ms, 10.4MB)
테스트 11 〉	통과 (0.00ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.4MB)
테스트 13 〉	통과 (0.02ms, 10.4MB)
테스트 14 〉	통과 (0.03ms, 10.4MB)
테스트 15 〉	통과 (0.02ms, 10.3MB)
'''

# 12121212 vs. 121121121
# 1200 1210
# 1211 1211
# 1212 1211
# 12121 vs 12112

from itertools import cycle

def pad_number(n):
    n_cycle = cycle(n)

    while len(n) < 4:
        n += next(n_cycle)
    
    return n

def solution(numbers):
    
    # 0만 나오는 경우 예외 처리
    if sum(numbers) == 0:
        return "0"
    
    numbers_list = [str(n) for n in numbers]
    numbers_list.sort(key = lambda x: -int(pad_number(x)))   
    
    return ''.join(numbers_list)

if __name__ == '__main__':
    l1 = [0, 2]
    l2 = [0, 1, 2]
    l3 = [0, 2, 3]
    print(l1 in l2)
    print(l1 in l3)