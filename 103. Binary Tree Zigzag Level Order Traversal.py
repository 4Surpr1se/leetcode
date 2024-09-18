from collections import deque
from typing import Optional, List

from utils import TreeNode


class Solution:

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return []
        q = deque([root])
        ans = []
        is_left_first = False
        while q:
            temp = []
            is_left_first = not is_left_first
            for i in range(len(q)):
                node = q.popleft()
                if is_left_first:
                    temp.append(node.val)
                else:
                    temp.insert(0, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(temp)
        return ans
