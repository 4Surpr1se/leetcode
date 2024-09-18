from typing import Optional

from utils import TreeNode


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # https://www.geeksforgeeks.org/binary-search-tree-traversal-inorder-preorder-post-order/
        def recr(root):
            min_list = [10 ** 5]
            if not root:
                return 10 ** 5
            if root.left:
                min_list.extend([recr(root.left), root.val - root.left.val])
            if root.right:
                min_list.extend([recr(root.right), root.right.val - root.val])
            return min(min_list)

        return recr(root)
