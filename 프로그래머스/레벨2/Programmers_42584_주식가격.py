def solution(prices):
    answer = [len(prices)-i-1 for i in range(len(prices))]
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[j] < prices[i]:  # 가격이 떨어진 경우
                answer[i] = j-i
                break
    return answer
