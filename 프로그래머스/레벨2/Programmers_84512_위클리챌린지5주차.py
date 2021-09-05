'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.3MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.3MB)
테스트 7 〉	통과 (0.00ms, 10.2MB)
테스트 8 〉	통과 (0.00ms, 10.1MB)
테스트 9 〉	통과 (0.00ms, 10.2MB)
테스트 10 〉	통과 (0.00ms, 10.2MB)
테스트 11 〉	통과 (0.00ms, 10.2MB)
테스트 12 〉	통과 (0.00ms, 10.2MB)
테스트 13 〉	통과 (0.00ms, 10.2MB)
테스트 14 〉	통과 (0.00ms, 10.2MB)
테스트 15 〉	통과 (0.00ms, 10.2MB)
테스트 16 〉	통과 (0.00ms, 10.3MB)
테스트 17 〉	통과 (0.00ms, 10.1MB)
테스트 18 〉	통과 (0.00ms, 10.2MB)
테스트 19 〉	통과 (0.00ms, 10.1MB)
테스트 20 〉	통과 (0.00ms, 10.2MB)
테스트 21 〉	통과 (0.00ms, 10.3MB)
테스트 22 〉	통과 (0.00ms, 10.1MB)
테스트 23 〉	통과 (0.00ms, 10.2MB)
테스트 24 〉	통과 (0.00ms, 10.2MB)
테스트 25 〉	통과 (0.00ms, 10.2MB)
테스트 26 〉	통과 (0.00ms, 10.1MB)
테스트 27 〉	통과 (0.00ms, 10.2MB)
테스트 28 〉	통과 (0.01ms, 10.3MB)
테스트 29 〉	통과 (0.00ms, 10.2MB)
테스트 30 〉	통과 (0.00ms, 10.2MB)
테스트 31 〉	통과 (0.00ms, 10.2MB)
테스트 32 〉	통과 (0.00ms, 10.2MB)
테스트 33 〉	통과 (0.00ms, 10.2MB)
테스트 34 〉	통과 (0.00ms, 10.2MB)
테스트 35 〉	통과 (0.00ms, 10.2MB)
테스트 36 〉	통과 (0.00ms, 10.2MB)
테스트 37 〉	통과 (0.01ms, 10.3MB)
테스트 38 〉	통과 (0.00ms, 10.2MB)
테스트 39 〉	통과 (0.00ms, 10.3MB)
테스트 40 〉	통과 (0.00ms, 10.2MB)
'''

def solution(word):
    answer = 0
    idx_dict = { 0: 780, 1: 155, 2: 30, 3: 5, 4: 1}
    char_dict = { "A": 0, "E": 1, "I": 2, "O": 3, "U": 4}
    for idx, char in enumerate(word):
        # print(idx, char, f'{answer}+ {idx_dict[idx]}*{char_dict[char]}+{char_dict[char] + 1}')
        if idx == 4:
            answer += idx_dict[idx] * char_dict[char] + 1
        else:
            answer += idx_dict[idx] * char_dict[char] + char_dict[char] + 1
            
    return answer