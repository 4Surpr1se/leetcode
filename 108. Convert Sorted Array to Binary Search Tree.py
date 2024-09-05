# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return TreeNode(val=nums[len(nums) // 2],
                        left=self.sortedArrayToBST(nums[:len(nums) // 2]),
                        right=self.sortedArrayToBST(nums[len(nums) // 2 + 1:])) if nums else None

    def sortedArrayToBSTNOTMINE_BUT_I_THOUGHT_ABOUT_IT(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = helper(start, mid - 1)
            root.right = helper(mid + 1, end)
            return root

        return helper(0, len(nums) - 1)

    def sortedArrayToBST_mine_kinda(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(start, end):
            return TreeNode(nums[(start + end) // 2], left=helper(start, (start + end) // 2 - 1),
                            right=helper((start + end) // 2 + 1, end)) if start > end else None

        return helper(0, len(nums) - 1)
