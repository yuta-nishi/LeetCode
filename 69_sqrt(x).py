# Time: O(log x)
# Space: O(1)


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left = 1
        right = x
        while left <= right:
            mid = left + (right - left) // 2
            if mid**2 < x:
                left = mid + 1
            elif mid**2 > x:
                right = mid - 1
            else:
                return mid
        return right
