from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recr(p, q):
            if not p and not q:
                return True

            if p and q and p.val == q.val:
                return recr(p.left, q.right) and recr(p.right, q.left)

            return False

        return recr(root.left, root.right) if root else None

    def isSymmetric_Not_Mine(self, root: Optional[TreeNode]) -> bool:
        return self.sym(root.left, root.right)

    def sym(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return root1.val == root2.val and self.sym(root1.left, root2.right) and self.sym(root1.right, root2.left)
