from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time: O(n)
# Space: O(n)
# Iterative


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset = {head}
        while head:
            head = head.next
            if head in hashset:
                return True
            else:
                hashset.add(head)
        return False


# Time: O(n)
# Space: O(1)
# Iterative


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
