'''
정확성  테스트
테스트 1 〉	통과 (4.51ms, 10.3MB)
테스트 2 〉	통과 (88.99ms, 11MB)
테스트 3 〉	통과 (85.23ms, 11.4MB)
테스트 4 〉	통과 (2.32ms, 10.3MB)
테스트 5 〉	통과 (64.55ms, 11MB)
테스트 6 〉	통과 (36.44ms, 11.2MB)
테스트 7 〉	통과 (2.24ms, 10.3MB)
테스트 8 〉	통과 (1.12ms, 10.3MB)
테스트 9 〉	통과 (0.91ms, 10.3MB)
테스트 10 〉	통과 (63.57ms, 10.5MB)
테스트 11 〉	통과 (9.43ms, 10.3MB)
테스트 12 〉	통과 (1.76ms, 10.3MB)
테스트 13 〉	통과 (47.05ms, 10.9MB)
테스트 14 〉	통과 (98.03ms, 11.2MB)
테스트 15 〉	통과 (29.88ms, 10.6MB)
테스트 16 〉	통과 (15.66ms, 10.6MB)
'''

def solution(arr1, arr2):
    # 곱할 수 있는 배열만 주어지므로 arr1_col == arr2_row
    arr1_row, arr1_col = len(arr1), len(arr1[0]) # arr1 행, 열
    arr2_row, arr2_col = len(arr2[0]), len(arr2) # arr2 행, 열
    
    answer = [[0 for _ in range(arr2_row)] for _ in range(arr1_row)]
    # print(answer)
    for r1 in range(arr1_row):
        # print(arr1[r1])
        for r2 in range(arr2_row):
            for c2 in range(arr2_col):
                # print(f"{arr1[r1][c2]} x {arr2[c2][r2]}")
                answer[r1][r2] += arr1[r1][c2]*arr2[c2][r2]    
    
    return answer