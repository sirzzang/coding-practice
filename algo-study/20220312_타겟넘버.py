'''
정확성  테스트
테스트 1 〉	통과 (158.96ms, 50MB)
테스트 2 〉	통과 (169.27ms, 49.5MB)
테스트 3 〉	통과 (0.16ms, 10.2MB)
테스트 4 〉	통과 (0.56ms, 10.3MB)
테스트 5 〉	통과 (4.66ms, 11.2MB)
테스트 6 〉	통과 (0.30ms, 10.2MB)
테스트 7 〉	통과 (0.27ms, 10.1MB)
테스트 8 〉	통과 (1.26ms, 10.4MB)
'''
def solution(numbers, target):
    sum_list = [0]
    for number in numbers:
        current_sum = []
        # 직전까지 순회한 number로 만들 수 있는 합에 현재 number를 더하고 뺀 값 기록
        for prev_sum in sum_list:
            current_sum.append(prev_sum + number)
            current_sum.append(prev_sum - number)
        
        # 합 리스트 교체
        sum_list = current_sum
    return sum_list.count(target)