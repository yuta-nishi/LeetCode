# n=len(nums)
# Time: O(nlogk)
# Space: O(n)

from collections import Counter
from heapq import nlargest
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        hash_table = Counter(nums)
        print(hash_table.keys())
        result = nlargest(k, hash_table.keys(), key=hash_table.get)
        return result


# Time: O(nlogn)
# Space: O(n)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        hash_table = Counter(nums)
        hash_table_sorted = sorted(hash_table.keys(), key=hash_table.get, reverse=True)
        result = [hash_table_sorted[i] for i in range(k)]
        return result
