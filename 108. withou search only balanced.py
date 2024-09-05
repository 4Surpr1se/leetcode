from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def recr(index):
            return TreeNode(val=nums[index - 1], left=recr(2 * index), right=recr(2 * index + 1)) if len(
                nums) >= index else None

        return recr(1)
