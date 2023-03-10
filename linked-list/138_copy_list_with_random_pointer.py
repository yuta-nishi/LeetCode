from typing import Optional


class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


# Time: O(n)
# Space: O(n)


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        hashmap = {None: None}
        cur = head
        while cur:
            copy = Node(cur.val)
            hashmap[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = hashmap[cur]
            copy.next = hashmap[cur.next]
            copy.random = hashmap[cur.random]
            cur = cur.next
        return hashmap[head]
