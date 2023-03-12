import collections

# n=len(s)
# m=26
# Time: O(n)
# Space: O(m)


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = collections.defaultdict(int)
        res = 0
        for right in range(len(s)):
            count[s[right]] += 1
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
