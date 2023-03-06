# n=len(temperatures)
# Time: O(n)
# Space: O(n)

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stack_idx, _ = stack.pop()
                res[stack_idx] = i - stack_idx
            stack.append([i, temp])
        return res
