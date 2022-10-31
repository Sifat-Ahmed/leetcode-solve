# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ## left -> root -> right
        result = list()

        def traverse(root):
            if root is None:
                return

            ## first recursively go to the left most child
            traverse(root.left)
            ## append the value
            result.append(root.val)
            ## now traverse the right most child
            traverse(root.right)

        traverse(root)

        return result