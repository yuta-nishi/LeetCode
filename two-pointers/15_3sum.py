# n=len(nums)
# Time: O(n^2)
# Space: O(n)

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for left in range(len(nums) - 2):
            if left > 0 and nums[left] == nums[left - 1]:
                continue
            mid = left + 1
            right = len(nums) - 1
            while mid < right:
                three_sum = nums[left] + nums[mid] + nums[right]
                if three_sum < 0:
                    mid += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    result.append([nums[left], nums[mid], nums[right]])
                    mid += 1
                    while mid < right and nums[mid] == nums[mid - 1]:
                        mid += 1
        return result
