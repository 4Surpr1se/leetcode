from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head
        tmp = head
        pos = 1
        storage = [tmp]
        while True:
            if not tmp.next and pos != 1:
                tmp.next = head
                len_ = pos
                break
            tmp = tmp.next
            storage.append(tmp)
            pos += 1
        tmp = storage[len_ - (k % len_) - 1]
        ret = tmp.next
        tmp.next = None
        return ret


tmp = None
list1 = []
for i in reversed([1, 2, 3, 4, 5]):
    tmp = ListNode(i, next=tmp)
    list1.append(tmp)
list1 = list1[::-1]

re = Solution().rotateRight(list1[0], 2)
print(re.val)
while re:
    print(re.val, end=' ')
    re = re.next
print(re)
