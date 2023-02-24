# n=len(strs)
# m=len(string)
# Time: O(n*m)
# Space: O(n*m)

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
