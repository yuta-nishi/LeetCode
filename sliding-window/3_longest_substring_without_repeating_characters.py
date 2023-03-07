# n=len(s)
# m=26
# Time: O(n)
# Space: O(min(m, n))


import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        hashmap = collections.defaultdict(int)
        res = 0
        while right < len(s):
            hashmap[s[right]] += 1
            while hashmap[s[right]] > 1:
                hashmap[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res
