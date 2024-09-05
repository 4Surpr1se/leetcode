# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head = list1 if list1.val < list2.val else list2
        tmp_link = list2 if list1.val < list2.val else list1
        while tmp:
            if not tmp.next:
                tmp.next = tmp_link
                break
            if tmp_link.val < tmp.next.val:
                tmp.next, tmp_link = tmp_link, tmp.next
            tmp = tmp.next
        return head


tmp = None
list1 = []
for i in reversed([-9, 3]):
    tmp = ListNode(i, next=tmp)
    list1.append(tmp)
list1 = list1[::-1]

tmp = None
list2 = []
for i in reversed([5, 7]):
    tmp = ListNode(i, next=tmp)
    list2.append(tmp)
list2 = list2[::-1]
re = Solution().mergeTwoLists(list1[0], list2[0])
while re:
    print(re.val, end=' ')
    re = re.next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if list1 else list2

        if list1.val > list2.val:
            list1, list2 = list2, list1

        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1