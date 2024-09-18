from collections import deque
from typing import Optional, List

from utils import TreeNode


class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return []
        q = deque([root])
        ans = []
        while q:
            temp = []
            for i in range(len(q)):
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(temp)
        return ans
