def solution(arr, divisor):
    arr.sort()
    answer = [elem for elem in arr if not elem % divisor]
    if answer:
        return answer
    else:
        return [-1]