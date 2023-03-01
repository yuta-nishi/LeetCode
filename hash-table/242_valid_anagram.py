# n=len(s)
# m=len(t)
# Time: O(n)
# Space: O(n+m)

from collections import Counter, defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count = defaultdict(int)
        t_count = defaultdict(int)
        for i in range(len(s)):
            s_count[s[i]] += 1
            t_count[t[i]] += 1
        if s_count == t_count:
            return True
        return False


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)
        t_count = Counter(t)
        if s_count == t_count:
            return True
        return False


# Time: O(nlog(n))
# Space: O(1)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sort = sorted(s)
        t_sort = sorted(t)
        if s_sort == t_sort:
            return True
        return False
