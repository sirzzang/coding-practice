'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.05ms, 10.3MB)
테스트 6 〉	통과 (0.05ms, 10.2MB)
테스트 7 〉	통과 (2.64ms, 10.3MB)
테스트 8 〉	통과 (1.07ms, 10.2MB)
테스트 9 〉	통과 (4.47ms, 10.3MB)
테스트 10 〉통과 (1.97ms, 10.3MB)
테스트 11 〉통과 (4.60ms, 10.3MB)
테스트 12 〉통과 (3.95ms, 10.3MB)
테스트 13 〉통과 (0.32ms, 10.3MB)
테스트 14 〉통과 (5.03ms, 10.3MB)
'''

def is_correct(pred, true):
    answer = 0
    for i in range(len(true)):
        answer += (pred[i%len(pred)] == true[i]) # boolean -> 숫자
    return answer    

def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [is_correct(first, answers), is_correct(second, answers), is_correct(third, answers)]
    
    return [i+1 for i, v in enumerate(scores) if v == max(scores)] # 인덱스 0번부터 시작함.

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (1.62ms, 10.3MB)
테스트 8 〉	통과 (0.69ms, 10.3MB)
테스트 9 〉	통과 (2.86ms, 10.3MB)
테스트 10 〉통과 (1.57ms, 10.3MB)
테스트 11 〉통과 (2.74ms, 10.2MB)
테스트 12 〉통과 (2.57ms, 10.3MB)
테스트 13 〉통과 (0.22ms, 10.2MB)
테스트 14 〉통과 (2.55ms, 10.3MB)
'''

def solution(answers):
    res = [0, 0, 0, 0]
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]        
    for i in range(len(answers)):
        if first[i%5] == answers[i]:
            res[1] += 1
        if second[i%8] == answers[i]:
            res[2] += 1
        if third[i%10] == answers[i]:
            res[3] += 1
    answer = []
    for i, v in enumerate(res):
        if v == max(res):
            answer.append(i)
    return answer