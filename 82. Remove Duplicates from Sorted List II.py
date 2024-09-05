from typing import Optional

from utils import to_linked_list, print_linked_list, ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = dummy = ListNode(0, head)
        last = prev.next
        while last:
            if last.next and last.val == last.next.val:
                last = last.next
                while last.next and last.val == last.next.val:
                    last = last.next
                last = prev.next = last.next
            else:
                prev = last
                last = last.next
        return dummy.next


re = Solution().deleteDuplicates(to_linked_list([1, 1])[0])
print_linked_list(re)
