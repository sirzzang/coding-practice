from typing import List

# 80ms, 14.6MB


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    merged_array = nums1 + nums2  # extend: O(n)
    if len(merged_array) == 1:
        return merged_array[0]

    merged_array.sort()
    idx = len(merged_array) // 2
    if len(merged_array) % 2 == 0:
        print((merged_array[idx-1] + merged_array[idx])/2)
    else:
        print(merged_array[idx])


findMedianSortedArrays([1, 3], [2])
findMedianSortedArrays([1, 2], [3, 4])
findMedianSortedArrays([0, 0], [0, 0])
