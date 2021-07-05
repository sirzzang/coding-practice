from typing import List, Tuple

# runtime error
'''
TypeError: collect() missing 1 required positional argument: 'height'
    return collect(l_height) + collect(r_height)
Line 31 in trap (Solution.py)
    ret = Solution().trap(param_1)
Line 52 in _driver (Solution.py)
    _driver()
Line 63 in <module> (Solution.py)
'''


class Solution:
    def split(self, height: List[int]) -> Tuple[List[int], List[int]]:
        max_height = max(height)
        max_idx = height.index(max_height)
        return height[:max_idx+1], height[max_idx:][::-1]

    def collect(self, height: List[int]) -> int:
        wall = 0
        water = 0
        for h in height:
            if h > wall:
                wall = h
            water += wall-h
        return water

    def trap(self, height: List[int]) -> int:
        l_height, r_height = split(height)
        return collect(l_height) + collect(r_height)


# accepted
'''
Runtime: 48 ms
Memory Usage: 14.9 MB
'''


class Solution:

    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        max_height = max(height)
        max_idx = height.index(max_height)
        l_height, r_height = height[:max_idx+1], height[max_idx:][::-1]

        def collect(height: List[int]) -> int:
            wall = 0
            water = 0
            for h in height:
                if h > wall:
                    wall = h
                water += wall-h
            return water

        return collect(l_height) + collect(r_height)
