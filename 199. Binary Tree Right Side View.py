from collections import deque
from typing import Optional, List

from utils import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return []
        q = deque([root])
        ans = []
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(node.val)
        return ans