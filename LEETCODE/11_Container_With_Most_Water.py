from typing import List

'''716ms, 27.7MB'''


def maxArea(height: List[int]) -> int:
    print()

    # if len(height) == 2:
    #     print(height[1] - height[0])

    left, right = 0, len(height) - 1
    answer = 0
    while left <= right:
        area = min(height[left], height[right]) * (right - left)
        if area > answer:
            answer = area

        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    print(answer)


maxArea([1, 1])
maxArea([4, 3, 2, 1, 4])
maxArea([1, 2, 1])
maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
