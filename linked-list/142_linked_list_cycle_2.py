from typing import Optional


class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next


# Time: O(n)
# Space: O(n)


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        while head != slow:
            head = head.next
            slow = slow.next
        return head
