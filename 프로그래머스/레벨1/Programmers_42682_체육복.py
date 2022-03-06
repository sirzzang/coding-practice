'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.02ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.1MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
'''


def solution(n, lost, reserve):

    # 체육복 보유 상태
    students = [1] * n
    for l in lost:
        students[l-1] -= 1
    for r in reserve:
        students[r-1] += 1

    # 체육복이 없는 학생이 빌릴 수 있는지 체크
    for i in range(len(students)):
        if students[i] == 0:
            if i == 0:
                if students[i+1] > 1:  # 첫 번째 학생은 바로 뒤에서만 빌릴 수 있음.
                    students[i] += 1
                    students[i+1] -= 1
            elif 0 < i < len(students) - 1:  # 중간 학생은 앞, 뒤 중 한 사람에게서 빌릴 수 있음.
                if students[i-1] > 1:
                    students[i] += 1
                    students[i-1] -= 1
                    continue  # 앞에서 빌렸다면 계속 진행
                if students[i+1] > 1:
                    students[i] += 1
                    students[i+1] -= 1
            else:
                if students[i-1] > 1:  # 마지막 학생은 바로 앞에서만 빌릴 수 있음.
                    students[i] += 1
                    students[i-1] -= 1

    return n - students.count(0)
