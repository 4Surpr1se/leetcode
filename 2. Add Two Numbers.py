from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tmp_listnode = prev = None
        tmp_val1 = 0
        while l1 and l2:
            tmp_val2 = (l1.val + l2.val + tmp_val1) // 10
            tmp_listnode = ListNode((l1.val + l2.val) % 10 + tmp_val1)
            if prev:
                prev.next = tmp_listnode
            else:
                init = tmp_listnode
            prev = tmp_listnode
            tmp_val1 = tmp_val2
            l1 = l1.next

            print(prev.val)
        return init


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def rec(l1, l2):
            val = (l1.val + l2.val)
            if not val and not l1.next and not l2.next:
                return
            if not l1.next:
                l1.next = ListNode(0)
            if not l2.next:
                l2.next = ListNode(0)
            tmp_listnode = ListNode(val % 10)
            l1.next.val += val // 10
            tmp_listnode.next = rec(l1.next, l2.next)
            return tmp_listnode

        return rec(l1, l2) or ListNode(0)


tmp = None
list1 = []
for i in reversed([9, 9, 9, 9]):
    tmp = ListNode(i, next=tmp)
    list1.append(tmp)
list1 = list1[::-1]

tmp = None
list2 = []
for i in reversed([9, 9, 9, 9, 9, 9, 9]):
    tmp = ListNode(i, next=tmp)
    list2.append(tmp)
list2 = list2[::-1]

re = Solution().addTwoNumbers(list1[0], list2[0])
print(re.val)
while re:
    print(re.val, end=' ')
    re = re.next
print(re)
