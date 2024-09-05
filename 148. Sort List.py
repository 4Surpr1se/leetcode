from typing import Optional

from utils import ListNode, to_linked_list, print_linked_list, list_, list_2


class Solution:
    # merge и heap
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy_left = left = ListNode(-10 ** 6)
        dummy_right = right = ListNode(-10 ** 6)
        mid = head
        left_changed = right_changed = False
        while head:
            if head.val > mid.val:
                right.next, head = head, head.next
                right = right.next
                right_changed = True
            elif head.val < mid.val:
                left.next, head = head, head.next
                left = left.next
                left_changed = True
            elif head != mid and head.val == mid.val:
                left.next, head = head, head.next
                left = left.next
            else:
                head = head.next
        left.next = None
        right.next = None
        if right == dummy_right:
            pass
        if left_changed:
            dummy_left.next = self.sortList(dummy_left.next)
            left = dummy_left
            while left.next:
                left = left.next
        if right_changed and left == dummy_left:
            mid.next = self.sortList(dummy_right.next)
        else:
            mid.next = dummy_right.next
        left.next = mid
        return dummy_left.next

    def quicksortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-10 ** 6)
        dummy.next = head
        return self.partition(head)[0]

    # def partition(self, head):
    #     left_start = left = ListNode(-10 ** 6)
    #     right_start = right = ListNode(-10 ** 6)
    #     mid = head
    #     while head:
    #         if head.val > mid.val:
    #             right.next, head = head, head.next
    #         if head.val < mid.val:
    #             left.next, head = head, head.next
    #     left_start, left = self.partition(left_start.next)
    #     right_start, right = self.partition(right_start.next)
    #     left.next = mid
    #     mid.next = right_start
    #     return mid, right

    def partition_from_left_working_asf(self, head):
        if not head:
            return head
        dummy_left = left = ListNode(-10 ** 6)
        dummy_right = right = ListNode(-10 ** 6)
        mid = head
        while head:
            if head.val > mid.val:
                right.next, head = head, head.next
                right = right.next
            elif head.val < mid.val:
                left.next, head = head, head.next
                left = left.next
            else:
                head = head.next
        left.next = None
        right.next = None
        the_left = left
        dummy_left.next = self.partition_from_left_working_asf(dummy_left.next)
        mid.next = self.partition_from_left_working_asf(dummy_right.next)
        the_left.next = mid
        return dummy_left.next

    def partition(self, head):
        if not head:
            return head, head
        dummy_left = left = ListNode(-10 ** 6)
        dummy_right = right = ListNode(-10 ** 6)
        mid = head
        while head:
            if head.val > mid.val:
                right.next, head = head, head.next
                right = right.next
            elif head.val < mid.val:
                left.next, head = head, head.next
                left = left.next
            elif head != mid and head.val == mid.val:
                left.next, head = head, head.next
                left = left.next
            else:
                head = head.next
        left.next = None
        right.next = None

        print_linked_list(dummy_left.next)
        print_linked_list(dummy_right.next)
        dummy_left.next, left = self.partition(dummy_left.next)
        # left = dummy_left
        # while left.next:
        #     left = left.next
        mid.next, right = self.partition(dummy_right.next)
        if left:
            left.next = mid
        # print_linked_list(dummy_left.next)
        return dummy_left.next, right


input = to_linked_list(list_2)[0]
print_linked_list(Solution().sortList(input))
