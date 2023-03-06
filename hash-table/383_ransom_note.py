# n=len(ransomNote)
# Time: O(n)
# Space: O(n)


import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap1 = collections.defaultdict(int)
        hashmap2 = collections.defaultdict(int)
        for c in ransomNote:
            hashmap1[c] += 1
        for c in magazine:
            hashmap2[c] += 1
        for c in hashmap1:
            if hashmap1[c] > hashmap2[c]:
                return False
        return True
