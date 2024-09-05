# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from idlelib.tree import TreeNode
from typing import Optional


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def recursion(left, right):
            if not left and not right:
                return True
            if (not left and right) or (left and not right) or (left.val != right.val):
                return False
            return recursion(left.left, right.left) and recursion(left.right, right.right)

        return recursion(p, q)

    def isSameTreeNotMine(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            return self.isSameTreeNotMine(p.left, q.left) and self.isSameTreeNotMine(p.right, q.right)

        return False
