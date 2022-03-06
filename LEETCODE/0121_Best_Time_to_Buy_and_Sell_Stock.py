from typing import List


def maxProfit(prices: List[int]) -> int:
    low, high = 10**4 + 1, -1
    for price in prices:
        # 저점 갱신
        if price < low:
            if high == -1:  # 고점 없을 때
                low = price
            else:
                low, high = price, price
        # 고점
        else:
            if price >= high:
                high = price
        print(f"price: {price}, low: {low}, high: {high}")
    print(low, high)
    print()


maxProfit([7, 1, 5, 3, 6, 4])
maxProfit([1, 2, 3, 4, 5])
maxProfit([7, 6, 4, 3, 1])
maxProfit([7, 8, 8, 8, 8])
maxProfit([7, 7, 7, 7, 7])
maxProfit([2, 4, 1])  # 3개인데 price <= low인 경우가 문제
maxProfit([2, 4, 3])
maxProfit([7, 1, 5])
maxProfit([3, 5, 6, 2])
maxProfit([2, 1, 2, 0, 1])
