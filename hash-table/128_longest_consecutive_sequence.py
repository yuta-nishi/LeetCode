# n=len(nums)
# Time: O(n)
# Space: O(n)

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_count = 0
        for num in num_set:
            if num - 1 not in num_set:
                cur_num = num
                count = 1
                while cur_num + 1 in num_set:
                    cur_num += 1
                    count += 1
                max_count = max(max_count, count)
        return max_count
