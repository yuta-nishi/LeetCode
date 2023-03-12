from typing import List


# Time: O(n)
# Space: O(n)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashset = set()
        for num in nums:
            if num not in hashset:
                hashset.add(num)
            else:
                return num


# Time: O(nlogn)
# Space: O(n)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        for i in range(1, len(nums)):
            if sorted_nums[i] == sorted_nums[i - 1]:
                return sorted_nums[i]


# Time: O(n)
# Space: O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            cur = abs(num)
            if nums[cur] < 0:
                res = cur
                break
            nums[cur] = -nums[cur]
        for num in nums:
            num = abs(num)
        return res


# Time: O(nlogn)
# Space: O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low = 1
        high = len(nums)
        while low <= high:
            mid = low + (high - low) // 2
            count = sum(num <= mid for num in nums)
            if count > mid:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res


# Time: O(n)
# Space: O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        head = nums[0]
        while head != slow:
            head = nums[head]
            slow = nums[slow]
        return head
