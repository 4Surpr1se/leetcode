class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def to_linked_list(list_):
    tmp = None
    return_list = []
    for i in reversed(list_):
        tmp = ListNode(i, next=tmp)
        return_list.append(tmp)
    return return_list[::-1]


def print_linked_list(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print(head)
