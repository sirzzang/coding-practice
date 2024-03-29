def solution(arr1, arr2):
    return [[arr1[row][col] + arr2[row][col]
             for col in range(len(arr1[0]))] for row in range(len(arr1))]

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.07ms, 10.3MB)
테스트 3 〉	통과 (0.21ms, 10.1MB)
테스트 4 〉	통과 (0.12ms, 10.2MB)
테스트 5 〉	통과 (0.06ms, 10.2MB)
테스트 6 〉	통과 (0.21ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.1MB)
테스트 8 〉	통과 (0.08ms, 10.3MB)
테스트 9 〉	통과 (0.80ms, 10.9MB)
테스트 10 〉	통과 (0.60ms, 10.6MB)
테스트 11 〉	통과 (0.40ms, 10.4MB)
테스트 12 〉	통과 (0.48ms, 10.5MB)
테스트 13 〉	통과 (0.40ms, 10.7MB)
테스트 14 〉	통과 (0.47ms, 10.6MB)
테스트 15 〉	통과 (0.54ms, 10.5MB)
테스트 16 〉	통과 (0.49ms, 10.6MB)
테스트 17 〉	통과 (24.50ms, 22.8MB)
'''