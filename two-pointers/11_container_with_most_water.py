# n=len(height)
# Time: O(n)
# Space: O(1)

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        result = 0
        while left < right:
            min_height = min(height[left], height[right])
            width = right - left
            area = min_height * width
            result = max(result, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return result
