# hash 자료 구조 이용한 풀이
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.00ms, 10.1MB)
테스트 4 〉	통과 (0.00ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.00ms, 10.2MB)
테스트 9 〉	통과 (0.00ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.00ms, 10.1MB)
테스트 13 〉	통과 (0.00ms, 10.1MB)
테스트 14 〉	통과 (1.09ms, 10.4MB)
테스트 15 〉	통과 (1.45ms, 10.3MB)
테스트 16 〉	통과 (6.20ms, 10.4MB)
테스트 17 〉	통과 (6.61ms, 10.3MB)
테스트 18 〉	통과 (4.46ms, 10.3MB)
테스트 19 〉	통과 (2.12ms, 10.3MB)
테스트 20 〉	통과 (4.00ms, 10.5MB)
효율성  테스트
테스트 1 〉	통과 (1.00ms, 11.3MB)
테스트 2 〉	통과 (0.89ms, 11.1MB)
테스트 3 〉	통과 (383.85ms, 41.3MB)
테스트 4 〉	통과 (174.16ms, 39.2MB)
'''
def solution(phone_book):
    # hash 자료 구조 안에서 있는지 검사
    hash_set = set(phone_book)
    
    for number in phone_book:
        prefix = ""        
        for n in number:
            prefix += n
            # prefix가 전화번호부에 있고 전체 번호가 아닐 때
            if prefix in hash_set and prefix != number:
                return False
    
    
    return True


# 시간 초과 풀이
def solution(phone_book):
    for i in range(len(phone_book)):
        flag = phone_book[i]
        for v in phone_book[:i] + phone_book[i+1:]:
            # 맨 앞에 나오는 경우
            if v.find(flag) == 0:
                return False
    return True