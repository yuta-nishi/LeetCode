# n=len(nums)
# Time: O(n)
# Space: O(n)

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_num = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dict_num:
                return dict_num[complement], i
            dict_num[nums[i]] = i
