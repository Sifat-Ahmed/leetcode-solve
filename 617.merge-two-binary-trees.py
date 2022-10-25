# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        ## dfs???

        def dfs(node1, node2):
            if node1 and node2:
                ## create a new tree with the combined values
                root = TreeNode(node1.val + node2.val)
                ## pass the left pairs to root.left
                root.left = dfs(node1.left, node2.left)
                ## pass the right pairs to root right
                root.right = dfs(node1.right, node2.right)

                return root

            else:
                ## if both nodes are not present, send the available one because we need two to join
                return node1 or node2

        return dfs(root1, root2)