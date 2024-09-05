from typing import Optional

from utils import to_linked_list, print_linked_list, ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        head = tmp = dummy
        pos = 0
        while tmp.next:
            tmp = tmp.next
            pos += 1
        for _ in range(pos - n):
            head = head.next
        head.next = head.next.next
        return dummy.next

    def removeNthFromEnd_BETTER_NOT_MINE(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        dummy = res

        for _ in range(n):
            head = head.next

        while head:
            head = head.next
            dummy = dummy.next

        dummy.next = dummy.next.next

        return res.next


re = Solution().removeNthFromEnd(to_linked_list([1, 2, 3, 4, 5])[0], 2)
print_linked_list(re)
