from typing import Optional

from utils import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            mx = 1
        else:
            return 0

        def recur(root, index):
            nonlocal mx
            if index > mx:
                mx = index
            if root.left:
                recur(root.left, index + 1)
            if root.right:
                recur(root.right, index + 1)
        recur(root, 1)
        return mx