# n=len(piles)
# m=max(piles)
# Time: O(nlogm)
# Space: O(1)


import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left <= right:
            mid = left + (right - left) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            if hours <= h:
                right = mid - 1
                res = mid
            else:
                left = mid + 1
        return res
