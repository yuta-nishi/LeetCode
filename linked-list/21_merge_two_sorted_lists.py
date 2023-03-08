class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


# n=len(min(list1, list2))
# Time: O(n)
# Space; O(1)
# Iterative


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next


# Time: O(n)
# Space; O(n)
# Recursive


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 and list2:
            if list1.val < list2.val:
                head = list1
                list1 = list1.next
            else:
                head = list2
                list2 = list2.next
            head.next = self.mergeTwoLists(list1, list2)
            return head
        else:
            if list1:
                return list1
            elif list2:
                return list2
