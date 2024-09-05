# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pos = 1
        tmp = head
        before = last = prev = None
        while pos != left:
            pos += 1
            before = tmp
            tmp = tmp.next
        first = tmp
        while pos != right + 1:
            if pos == right:
                last = tmp
            pos += 1
            tmp.next, prev, tmp = prev, tmp, tmp.next
        first.next = tmp
        if before:
            before.next = last
            return head
        else:
            return last

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        cur = prev.next
        for _ in range(right - left):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next

tmp = None
list1 = []
for i in reversed([1,2,3,4,5, 6, 7]):
    tmp = ListNode(i, next=tmp)
    list1.append(tmp)
list1 = list1[::-1]

re = Solution().reverseBetween(list1[0], 2, 6)
# re
# print(re.val)
while re:
    print(re.val, end=' ')
    re = re.next
print(re)
