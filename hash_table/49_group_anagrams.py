# n=len(strs)
# m=len(string)
# Time: O(nm)
# Space: O(nm)

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = defaultdict(list)
        for string in strs:
            char_count = [0] * 26
            for char in string:
                char_count[ord(char) - ord("a")] += 1
            hash_table[tuple(char_count)].append(string)
        return hash_table.values()


# Time: O(nmlog(m))
# Space: O(nm)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = defaultdict(list)
        for string in strs:
            hash_table[tuple(sorted(string))].append(string)
        return hash_table.values()
