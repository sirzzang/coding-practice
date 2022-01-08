'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.00ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.4MB)
테스트 15 〉	통과 (0.01ms, 10.3MB)
테스트 16 〉	통과 (0.01ms, 10.3MB)
테스트 17 〉	통과 (0.01ms, 10.3MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	통과 (0.01ms, 10.3MB)
테스트 20 〉	통과 (0.01ms, 10.2MB)
'''

def solution(n, lost, reserve):
    
    lost.sort()
    reserve.sort()
    
    lost_real = [l for l in lost if l not in reserve]
    reserve_real = [r for r in reserve if r not in lost]
    
    
    for r in reserve_real:
        
        print(r, lost_real, reserve_real)

        # 앞 사람에게 빌려줄 수 있는 경우
        if r - 1 in lost_real:
            lost_real.remove(r - 1)
            continue
            
        # 뒷 사람에게 빌려줄 수 있는 경우
        if r + 1 in lost_real:
            lost_real.remove(r + 1)
            
    print(lost_real, reserve_real)
    return n - len(lost_real)

solution(5, [2, 4], [5, 3])