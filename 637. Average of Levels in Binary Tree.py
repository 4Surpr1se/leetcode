
from collections import deque
from typing import List, Optional

from utils import TreeNode


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = []

        queue.append(root)
        power = counter = sum_ = nonreg = 0
        res = []
        while queue:
            root = queue.pop(0)
            if root:
                sum_ += root.val
                queue.extend([root.left, root.right])
            else:
                nonreg += 1
            counter += 1
            if 2 ** power == counter:
                if 2 ** power == nonreg:
                    break
                res.append(sum_ / (2 ** power - nonreg))
                power += 1
                sum_ = 0
                nonreg = counter = nonreg * 2
        return res


class Solution:
    # Лучше решение точно,
    # просто запоминаем на каждом этапе скок у нас в очереди лежит
    # и среднее этого количества и считаем
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        ans = []
        while q:
            qlen = len(q)
            row = 0
            for i in range(qlen):
                node = q.popleft()
                row += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(row / qlen)
        return ans
