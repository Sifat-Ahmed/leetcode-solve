# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return

        queue = [root]
        result = list()

        while queue:
            level = list()

            for _ in range(len(queue)):
                node = queue.pop(0)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

                level.append(node.val)

            result.append(level)

        return result