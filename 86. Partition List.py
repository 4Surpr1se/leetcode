# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from utils import ListNode, to_linked_list, print_linked_list


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        prev = dummy = ListNode(0, head)
        tmp = summer = None
        pointer = prev.next

        while pointer:
            if pointer.val < x:
                prev.next = prev = pointer
                pointer = pointer.next
                prev.next = None
            else:
                if not tmp:
                    tmp = summer = pointer
                    pointer = pointer.next
                else:
                    v = pointer.next
                    tmp.next = pointer
                    tmp = tmp.next
                    pointer = v
                    tmp.next = None

        prev.next = summer
        return dummy.next

    def partitionNotMine(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before, after = ListNode(0), ListNode(0)
        before_curr, after_curr = before, after

        while head:
            if head.val < x:
                before_curr.next, before_curr = head, head
            else:
                after_curr.next, after_curr = head, head
            head = head.next

        after_curr.next = None
        before_curr.next = after.next

        return before.next


print_linked_list(Solution().partition(to_linked_list([1,4,3,2,5,2])[0], 3))
