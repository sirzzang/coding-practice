from typing import List

'''88ms, 14.9MB'''


def maxProfit(prices: List[int]) -> int:
    print()
    profit = 0
    stack = []

    for price in prices:
        if not stack:
            stack.append(price)
        else:
            if price < stack[-1]:
                if len(stack) == 1:
                    stack.pop()
                    stack.append(price)
                else:
                    profit += (stack[-1]-stack[0])
                    stack = [price]
            elif price > stack[-1]:
                stack.append(price)
        print(f"price: {price}, stack: {stack}, profit: {profit}")

    if len(stack) >= 2:
        return profit + (stack[-1]-stack[0])
    else:
        return profit


maxProfit([7, 1, 5, 3, 6, 4])
maxProfit([1, 2, 3, 4, 5])
maxProfit([7, 6, 4, 3, 1])
maxProfit([7, 8, 8, 8, 8])
maxProfit([7, 7, 7, 7, 7])
maxProfit([2, 4, 1])
maxProfit([7, 1, 5])
