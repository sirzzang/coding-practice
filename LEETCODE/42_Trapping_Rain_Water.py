from typing import List, Tuple


def split(height: List[int]) -> Tuple[List[int], List[int]]:
    max_height = max(height)
    max_idx = height.index(max_height)
    return height[:max_idx+1], height[max_idx:][::-1]


def collect(height: List[int]) -> int:
    wall = 0
    water = 0
    for h in height:
        if h > wall:
            wall = h
        water += wall-h
    return water


def trap(height: List[int]) -> int:
    l_height, r_height = split(height)
    print(collect(l_height))
    print(collect(r_height))
    return collect(l_height) + collect(r_height)


# l, r = split([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 4, 2, 1, 0, 2, 1, 0, 1])
trap([4, 2, 0, 3, 2, 5])
trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 4, 2, 1, 0, 2, 1, 0, 1])
